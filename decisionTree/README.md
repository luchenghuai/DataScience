# Decision Tree (PyTorch + pandas)

A from-scratch decision tree classifier implemented with **PyTorch tensors**
for all numerical work and **pandas** for reading the training data from CSV.

This is a classic CART-style ("Classification And Regression Tree")
decision tree: it greedily picks the feature/threshold split that reduces
[Gini impurity](https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity)
the most at every node, and recurses until a stopping condition is met.

> **Note:** This is *not* a differentiable "soft" decision tree. PyTorch is
> used purely as a tensor computation library (masking, counting, comparing)
> so the whole pipeline shares one tensor engine — no `autograd`,
> `.backward()`, or gradient-based optimization is involved anywhere. Tree
> construction is a discrete, greedy search, exactly like scikit-learn's
> `DecisionTreeClassifier`, just reimplemented on top of `torch.Tensor`
> instead of NumPy.

## Files

| File               | Purpose                                                                 |
|--------------------|--------------------------------------------------------------------------|
| `decision_tree.py` | The `DecisionTreeClassifier` and `Node` classes (the actual algorithm). |
| `train.py`         | Loads `X_train.csv`/`y_train.csv` with pandas, trains, prints the tree, reports accuracy. |
| `X_train.csv`      | Training features (inputs).                                             |
| `y_train.csv`      | Training labels (target/output).                                        |

## Running it

```bash
pip install torch pandas
python train.py
```

Expected output: the learned tree structure printed as nested `[feature <=
threshold]` splits, followed by the training accuracy (100% on this toy
dataset, since the tree is allowed to grow deep enough to perfectly fit
only 14 examples).

## The dataset: "Play Tennis"

This is the classic, textbook decision-tree teaching example: given the
weather conditions on a given day, predict whether tennis was played. It's
small (14 rows) and every feature is categorical, which makes the resulting
tree easy to read and sanity-check by hand.

### `X_train.csv` — input features

Each row is one day's weather observation. Categorical values are
label-encoded as integers so they can be loaded straight into a
`torch.FloatTensor` (the tree treats them as thresholds to split on, the
same way scikit-learn does internally).

| Column        | Meaning                          | Encoding                                  |
|---------------|-----------------------------------|--------------------------------------------|
| `Outlook`     | General weather outlook           | `Sunny=0`, `Overcast=1`, `Rain=2`          |
| `Temperature` | Temperature category              | `Hot=0`, `Mild=1`, `Cool=2`                |
| `Humidity`    | Humidity level                    | `High=0`, `Normal=1`                       |
| `Wind`        | Wind strength                     | `Weak=0`, `Strong=1`                       |

### `y_train.csv` — target/output

A single column, `PlayTennis`, aligned row-for-row with `X_train.csv`:

| Value | Meaning |
|-------|---------|
| `0`   | No, tennis was not played that day |
| `1`   | Yes, tennis was played that day |

### Human-readable version of the data

| Day | Outlook  | Temperature | Humidity | Wind   | PlayTennis |
|-----|----------|-------------|----------|--------|------------|
| 1   | Sunny    | Hot         | High     | Weak   | No         |
| 2   | Sunny    | Hot         | High     | Strong | No         |
| 3   | Overcast | Hot         | High     | Weak   | Yes        |
| 4   | Rain     | Mild        | High     | Weak   | Yes        |
| 5   | Rain     | Cool        | Normal   | Weak   | Yes        |
| 6   | Rain     | Cool        | Normal   | Strong | No         |
| 7   | Overcast | Cool        | Normal   | Strong | Yes        |
| 8   | Sunny    | Mild        | High     | Weak   | No         |
| 9   | Sunny    | Cool        | Normal   | Weak   | Yes        |
| 10  | Rain     | Mild        | Normal   | Weak   | Yes        |
| 11  | Sunny    | Mild        | Normal   | Strong | Yes        |
| 12  | Overcast | Mild        | High     | Strong | Yes        |
| 13  | Overcast | Hot         | Normal   | Weak   | Yes        |
| 14  | Rain     | Mild        | High     | Strong | No         |

## How the algorithm works (`decision_tree.py`)

1. **Gini impurity** (`_gini`): for a set of labels at a node, computes
   `1 - sum(p_c^2)` over class fractions `p_c`. `0` means the node is
   perfectly pure (all one class); higher values mean more mixed classes.

2. **Finding the best split** (`_best_split`): for every feature column,
   tries every distinct value in that column as a candidate threshold.
   Samples with `feature <= threshold` go left, the rest go right. The
   split that produces the lowest *weighted* Gini impurity across the two
   children (equivalently, the highest "information gain" over the
   parent's impurity) is selected.

3. **Recursive construction** (`_build_tree`): starting at the root with
   all training samples, repeatedly finds the best split and recurses on
   the left/right partitions, until:
   - the node is already pure (only one class present), or
   - fewer than `min_samples_split` samples remain, or
   - `max_depth` has been reached, or
   - no split improves impurity at all.

   When recursion stops, the node becomes a **leaf** storing the
   majority class label of the samples that reached it.

4. **Prediction** (`predict` / `_predict_single`): a new sample is routed
   from the root down to a leaf by repeatedly comparing
   `sample[feature_index] <= threshold` at each decision node, then
   returning that leaf's stored class label.

5. **Inspecting the tree** (`print_tree`): recursively prints the tree as
   nested `[feature <= threshold]` decision nodes and `leaf -> class N`
   terminals, so you can read the learned decision logic directly.

## Extending this example

- **Bigger/real datasets**: replace `X_train.csv`/`y_train.csv` with your
  own data (same two-file convention: aligned rows, header row with
  column names). Continuous numeric features work as-is — the threshold
  search (`torch.unique(column)`) naturally handles them too.
- **Held-out evaluation**: `train.py` currently only reports training
  accuracy. For anything beyond a teaching example, split off an
  `X_test.csv`/`y_test.csv` and call `tree.predict(X_test)` to get an
  honest accuracy estimate.
- **Pruning / regularization**: tune `max_depth` and `min_samples_split`
  in `train.py` to control overfitting on larger datasets.
