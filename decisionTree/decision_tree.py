"""
decision_tree.py
=================

A from-scratch implementation of a CART-style ("Classification And
Regression Tree") decision tree classifier.

Why PyTorch instead of NumPy / scikit-learn?
---------------------------------------------
Every numerical operation in this file (impurity calculations, masking,
counting, comparisons) is done with `torch.Tensor` objects instead of
Python lists or NumPy arrays. This is purely so the whole pipeline -
loading data, training, and predicting - runs on the same tensor engine
that the rest of a PyTorch project would use (and could, in principle, be
moved onto a GPU with `.to("cuda")`).

Important: this is a *classic*, greedy, discrete decision tree - NOT a
differentiable "soft" decision tree. We never call `.backward()` or use
`requires_grad=True` anywhere, because the tree-building algorithm makes
hard (non-differentiable) yes/no decisions about how to split the data.
PyTorch is used here simply as a tensor computation library, not as an
autograd/optimization engine.

The algorithm implemented is the standard recursive splitting procedure:
    1. Start with all training samples at the root node.
    2. Try every (feature, threshold) pair and measure how much splitting
       on it would reduce Gini impurity.
    3. Keep the split that reduces impurity the most.
    4. Recurse on the left and right partitions until a stopping
       condition is met (max depth reached, node is pure, or too few
       samples remain).
    5. Nodes that stop splitting become "leaves" that store the majority
       class label of the samples that landed in them.
"""

import torch


class Node:
    """
    A single node in the decision tree.

    A node is either:
      * an internal/decision node: holds a `feature_index` and a
        `threshold`. Samples are routed to `left` if
        sample[feature_index] <= threshold, otherwise to `right`.
      * a leaf node: holds a `value`, which is the predicted class label
        for any sample that reaches this node.

    We tell the two apart with `is_leaf()`, which just checks whether
    `value` was set.
    """

    def __init__(self, feature_index=None, threshold=None, left=None, right=None, *, value=None):
        # --- fields used only by internal/decision nodes ---
        self.feature_index = feature_index  # which column of X this node splits on
        self.threshold = threshold          # the split point (a scalar float)
        self.left = left                    # Node reached when feature <= threshold
        self.right = right                  # Node reached when feature >  threshold

        # --- field used only by leaf nodes ---
        self.value = value                  # predicted class label (an int)

    def is_leaf(self):
        """A node is a leaf if and only if it was given a prediction value."""
        return self.value is not None


class DecisionTreeClassifier:
    """
    A CART-style decision tree classifier for categorical/numeric features
    that computes splits by minimizing weighted Gini impurity.

    Parameters
    ----------
    max_depth : int
        Maximum number of splits allowed along any path from the root to
        a leaf. Prevents the tree from growing until every leaf is 100%
        pure, which would overfit a small dataset.
    min_samples_split : int
        A node will not be split further if it has fewer than this many
        samples - it becomes a leaf instead.
    """

    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None          # the root Node, set once `fit()` has run
        self.n_classes_ = None    # number of distinct class labels seen during fit

    # ------------------------------------------------------------------
    # Impurity calculation
    # ------------------------------------------------------------------
    @staticmethod
    def _gini(y):
        """
        Compute the Gini impurity of a set of labels `y`.

        Gini impurity = 1 - sum_c (p_c^2)
        where p_c is the fraction of samples in `y` that belong to class c.

        Intuition: if every sample in `y` belongs to the same class,
        impurity is 0 (perfectly "pure" node). If classes are evenly
        mixed, impurity approaches its maximum. We want each split to
        push the two resulting groups of labels toward purity.

        Parameters
        ----------
        y : torch.LongTensor of shape (n_samples,)
            Class labels for the samples currently in this node.

        Returns
        -------
        float : the Gini impurity, a scalar Python float in [0, 1).
        """
        if y.numel() == 0:
            return 0.0

        # torch.unique with return_counts=True gives us, for each distinct
        # label value that appears in y, how many times it appears.
        _, counts = torch.unique(y, return_counts=True)

        # Convert counts to probabilities (fraction of samples per class).
        probabilities = counts.float() / y.numel()

        # Gini = 1 - sum(p_c^2). torch.sum(probabilities ** 2) is a 0-d
        # tensor, so we call .item() to turn it into a plain Python float.
        gini = 1.0 - torch.sum(probabilities ** 2)
        return gini.item()

    # ------------------------------------------------------------------
    # Finding the best split at a node
    # ------------------------------------------------------------------
    def _best_split(self, X, y):
        """
        Search over every feature column and every unique value in that
        column (used as a candidate threshold) to find the single split
        that reduces Gini impurity the most.

        A "split" partitions the samples into:
            left  = samples where X[:, feature] <= threshold
            right = samples where X[:, feature] >  threshold

        For each candidate split we compute the *weighted* Gini impurity
        of the two children (weighted by how many samples fall in each
        child), and compare it against the parent node's impurity. The
        difference is the "information gain" of that split.

        Returns
        -------
        (best_feature_index, best_threshold, best_gain)
            best_feature_index : int or None if no split helps
            best_threshold     : float or None
            best_gain          : float, the impurity reduction achieved
        """
        n_samples, n_features = X.shape
        parent_gini = self._gini(y)

        best_gain = 0.0
        best_feature_index = None
        best_threshold = None

        # Try splitting on every feature (every column of X).
        for feature_index in range(n_features):
            column = X[:, feature_index]

            # Every distinct value present in this column is a candidate
            # threshold. (For a small, mostly-categorical dataset like
            # ours, this means we effectively try "is feature == this
            # category" splits, encoded as <= comparisons on integers.)
            candidate_thresholds = torch.unique(column)

            for threshold in candidate_thresholds:
                # Boolean masks selecting which rows go left vs. right.
                left_mask = column <= threshold
                right_mask = ~left_mask

                n_left = int(left_mask.sum().item())
                n_right = int(right_mask.sum().item())

                # Skip thresholds that don't actually split the data
                # (e.g. the largest value in the column sends everyone
                # left, leaving the right side empty).
                if n_left == 0 or n_right == 0:
                    continue

                gini_left = self._gini(y[left_mask])
                gini_right = self._gini(y[right_mask])

                # Weight each child's impurity by the fraction of samples
                # it received, so a split that isolates one tiny outlier
                # isn't rewarded just because that outlier is "pure".
                weighted_child_gini = (
                    (n_left / n_samples) * gini_left
                    + (n_right / n_samples) * gini_right
                )

                gain = parent_gini - weighted_child_gini

                if gain > best_gain:
                    best_gain = gain
                    best_feature_index = feature_index
                    best_threshold = threshold.item()

        return best_feature_index, best_threshold, best_gain

    # ------------------------------------------------------------------
    # Leaf value calculation
    # ------------------------------------------------------------------
    @staticmethod
    def _majority_class(y):
        """
        Return the most frequently occurring label in `y`. This becomes
        the prediction stored at a leaf node.
        """
        values, counts = torch.unique(y, return_counts=True)
        majority_index = torch.argmax(counts)
        return values[majority_index].item()

    # ------------------------------------------------------------------
    # Recursive tree construction
    # ------------------------------------------------------------------
    def _build_tree(self, X, y, depth):
        """
        Recursively build the tree starting from the samples (X, y)
        that have reached the current node, at recursion depth `depth`
        (the root is depth 0).
        """
        n_samples = y.numel()
        n_distinct_labels = torch.unique(y).numel()

        # --- Stopping conditions: turn this node into a leaf ---
        # 1) The node is already pure (only one class present).
        # 2) There are too few samples to justify another split.
        # 3) We've hit the maximum allowed tree depth.
        if (
            n_distinct_labels == 1
            or n_samples < self.min_samples_split
            or depth >= self.max_depth
        ):
            return Node(value=self._majority_class(y))

        # Otherwise, look for the best possible split at this node.
        feature_index, threshold, gain = self._best_split(X, y)

        # If no split improves impurity at all (gain <= 0), stop here too.
        if feature_index is None or gain <= 0:
            return Node(value=self._majority_class(y))

        # Partition the data according to the chosen split and recurse.
        column = X[:, feature_index]
        left_mask = column <= threshold
        right_mask = ~left_mask

        left_child = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        right_child = self._build_tree(X[right_mask], y[right_mask], depth + 1)

        return Node(
            feature_index=feature_index,
            threshold=threshold,
            left=left_child,
            right=right_child,
        )

    # ------------------------------------------------------------------
    # Public API: fit / predict
    # ------------------------------------------------------------------
    def fit(self, X, y):
        """
        Train the decision tree.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Feature matrix. Will be converted to a float32 torch.Tensor.
        y : array-like of shape (n_samples,)
            Integer class labels. Will be converted to a long torch.Tensor.
        """
        X_tensor = torch.as_tensor(X, dtype=torch.float32)
        y_tensor = torch.as_tensor(y, dtype=torch.long).view(-1)

        self.n_classes_ = torch.unique(y_tensor).numel()
        self.root = self._build_tree(X_tensor, y_tensor, depth=0)
        return self

    def _predict_single(self, x, node):
        """Walk one sample `x` down the tree from `node` until it hits a leaf."""
        if node.is_leaf():
            return node.value
        if x[node.feature_index] <= node.threshold:
            return self._predict_single(x, node.left)
        return self._predict_single(x, node.right)

    def predict(self, X):
        """
        Predict class labels for a batch of samples.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)

        Returns
        -------
        torch.LongTensor of shape (n_samples,) with the predicted class
        label for each row of X.
        """
        X_tensor = torch.as_tensor(X, dtype=torch.float32)
        predictions = [self._predict_single(row, self.root) for row in X_tensor]
        return torch.tensor(predictions, dtype=torch.long)

    # ------------------------------------------------------------------
    # Utility: print the learned tree structure
    # ------------------------------------------------------------------
    def print_tree(self, feature_names=None, node=None, depth=0):
        """
        Pretty-print the tree structure to stdout, e.g.:

            [Outlook <= 0.0]
              left:  [Humidity <= 0.0] ...
              right: leaf -> class 1
        """
        if node is None:
            node = self.root

        indent = "  " * depth

        if node.is_leaf():
            print(f"{indent}leaf -> class {node.value}")
            return

        feature_label = (
            feature_names[node.feature_index]
            if feature_names is not None
            else f"feature_{node.feature_index}"
        )
        print(f"{indent}[{feature_label} <= {node.threshold}]")
        print(f"{indent}left:")
        self.print_tree(feature_names, node.left, depth + 1)
        print(f"{indent}right:")
        self.print_tree(feature_names, node.right, depth + 1)
