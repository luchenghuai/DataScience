# decisionTree — Design Reference

> **Repo:** git@github.com:luchenghuai/DataScience.git
> **Branch:** main
> **Commit:** 1397715c

## Overview

`decisionTree` is a from-scratch, teaching-oriented implementation of a CART-style
("Classification And Regression Tree") decision tree classifier. All numerical work
(impurity calculations, masking, counting, comparisons) is done with `torch.Tensor`
operations rather than NumPy or scikit-learn, purely so the pipeline shares one
tensor engine end-to-end. It is a classic, discrete, greedy tree — no autograd,
`.backward()`, or `requires_grad` is used anywhere; PyTorch is a computation
library here, not an optimizer. The module trains and evaluates on the textbook
"Play Tennis" dataset (14 rows, 4 categorical features).

## Architecture

```
train.py                       decision_tree.py
┌─────────────────┐            ┌───────────────────────────┐
│ pandas.read_csv  │──rows───▶ │ DecisionTreeClassifier     │
│ (X_train, y_train)│           │  .fit(X, y)                │
└─────────────────┘            │    └─ _build_tree(...)      │
                                │         └─ _best_split(...) │
                                │              └─ _gini(...)  │
                                │  .predict(X)                │
                                │    └─ _predict_single(...)  │
                                │  .print_tree(...)           │
                                └──────────────┬──────────────┘
                                               │ builds/holds
                                               ▼
                                        ┌─────────────┐
                                        │    Node      │
                                        │ (tree of     │
                                        │  Node objs)  │
                                        └─────────────┘
```

| Type | File | Role |
|---|---|---|
| `Node` | `decision_tree.py` | A single tree node — either a decision node (`feature_index`, `threshold`, `left`, `right`) or a leaf (`value`). |
| `DecisionTreeClassifier` | `decision_tree.py` | Owns the fit/predict/print API and the recursive tree-building algorithm. |
| `train.py` | `train.py` | Script entry point: loads CSVs, trains a tree, prints its structure, reports accuracy. |

## Lifecycle

`decision_tree.py` exposes no long-running process — it is a plain library used
by a short-lived script (`train.py`):

1. **Load** — `train.py` reads `X_train.csv` / `y_train.csv` with pandas and
   converts them to `torch.float32` / `torch.long` tensors.
2. **Construct** — `DecisionTreeClassifier(max_depth=4, min_samples_split=2)`
   is instantiated; `root` is `None` and `n_classes_` is `None` until `fit()` runs.
3. **Fit** — `fit(X, y)` converts inputs to tensors, records `n_classes_`, and
   calls `_build_tree` recursively starting at `depth=0`, populating `self.root`.
4. **Inspect** — `print_tree()` walks the finished tree and prints it to stdout.
5. **Predict** — `predict(X)` walks each row of `X` from `root` to a leaf via
   `_predict_single` and returns the predicted labels as a tensor.
6. **Exit** — the script prints training accuracy and terminates; there is no
   persistence (no model save/load) and no teardown step.

## Public API / Interface

| Method | Signature | Purpose |
|---|---|---|
| `DecisionTreeClassifier.__init__` | `(max_depth=5, min_samples_split=2)` | Configure stopping conditions before training. |
| `DecisionTreeClassifier.fit` | `(X, y) -> self` | Train the tree on a feature matrix and integer label vector. |
| `DecisionTreeClassifier.predict` | `(X) -> torch.LongTensor` | Predict class labels for a batch of samples. |
| `DecisionTreeClassifier.print_tree` | `(feature_names=None, node=None, depth=0)` | Recursively print the learned tree as nested `[feature <= threshold]` / `leaf -> class N` lines. |
| `DecisionTreeClassifier._gini` (static) | `(y) -> float` | Weighted-impurity building block; not part of the intended public surface but referenced throughout. |
| `DecisionTreeClassifier._best_split` | `(X, y) -> (feature_index, threshold, gain)` | Internal search over all (feature, threshold) pairs. |
| `DecisionTreeClassifier._majority_class` (static) | `(y) -> int` | Internal leaf-value helper. |
| `Node.is_leaf` | `() -> bool` | True iff the node stores a prediction `value`. |

Only `fit`, `predict`, and `print_tree` are meant to be called from outside the
class; the underscore-prefixed methods are implementation details of the
recursive build/search algorithm.

## Core Flows

### Training (`fit` → `_build_tree`)

1. `fit` casts `X`/`y` to tensors and records `n_classes_`.
2. `_build_tree(X, y, depth)` checks stopping conditions on the current node's
   samples: single class present, sample count below `min_samples_split`, or
   `depth >= max_depth`. If any hold, return a leaf via `_majority_class(y)`.
3. Otherwise call `_best_split(X, y)`:
   - Compute `parent_gini = _gini(y)`.
   - For every feature column, take every distinct value as a candidate
     threshold; split into `left_mask = column <= threshold` / `right_mask = ~left_mask`.
   - Skip thresholds where one side is empty.
   - Compute the sample-weighted Gini of the two children and the resulting
     `gain = parent_gini - weighted_child_gini`.
   - Track the `(feature_index, threshold)` with the largest `gain`.
4. If no split achieves `gain > 0`, return a leaf (via `_majority_class(y)`).
5. Otherwise partition `X`/`y` by the winning split and recurse on each half
   at `depth + 1`, wiring the results into `Node(left=..., right=...)`.

### Prediction (`predict` → `_predict_single`)

1. `predict(X)` casts `X` to a `float32` tensor.
2. For each row, `_predict_single(x, node)` starts at `self.root` and, while
   `node` is not a leaf, compares `x[node.feature_index] <= node.threshold` to
   choose `node.left` or `node.right`.
3. Once a leaf is reached, its stored `value` is the prediction; results are
   collected into a `torch.LongTensor`.

### End-to-end script (`train.py`)

1. Read `X_train.csv` / `y_train.csv` with pandas; print row/column summary.
2. Convert to tensors; instantiate and `fit()` the tree (`max_depth=4`,
   `min_samples_split=2`).
3. `print_tree(feature_names=feature_names)` to show the learned splits.
4. `predict(X_train)` and compute training accuracy as `mean(predictions == y_train)`.

## State Machine

Each `Node` is in exactly one of two states, determined once at construction
and never mutated afterward:

| State | Determined by | Fields set | Behavior on predict |
|---|---|---|---|
| Decision node | `_build_tree` found `gain > 0` | `feature_index`, `threshold`, `left`, `right` | Routes the sample to `left` or `right` based on `x[feature_index] <= threshold`. |
| Leaf node | A stopping condition was met, or no split improved impurity | `value` | Returns `value` as the prediction; recursion terminates. |

`is_leaf()` (`node.value is not None`) is the sole discriminator; there is no
separate tag/enum, so a decision node must never also be assigned a `value`.

## Concurrency Model

Single-threaded and synchronous throughout: `_build_tree` recurses depth-first
on the Python call stack, and `predict` loops over rows one at a time. There is
no batching, vectorized traversal, threading, or async code. Tensors are
computed on CPU by default; the module makes no `.to("cuda")` calls itself but
nothing prevents moving `X`/`y` to a GPU device before calling `fit`/`predict`
since all operations are plain tensor ops.

## External Dependencies

| Dependency | Type | Purpose |
|---|---|---|
| `torch` | Python library | Tensor representation and operations (`unique`, masking, `argmax`, reductions) for impurity calculation, splitting, and prediction. |
| `pandas` | Python library | Reads `X_train.csv` / `y_train.csv` into DataFrames in `train.py`. |
| `X_train.csv` / `y_train.csv` | Local data files | The only data source; no database or network dependency. |

## Configuration

| Key | Type | Default | Purpose |
|---|---|---|---|
| `max_depth` | `int` | `5` (class default); `train.py` passes `4` | Maximum root-to-leaf split depth; caps overfitting. |
| `min_samples_split` | `int` | `2` | Minimum samples required at a node to attempt another split. |
| `X_train.csv` path | file path | `"X_train.csv"` (cwd-relative, hardcoded in `train.py`) | Input feature matrix. |
| `y_train.csv` path | file path | `"y_train.csv"` (cwd-relative, hardcoded in `train.py`) | Input label vector. |

There is no config file or environment-variable surface; all tuning happens by
editing the literal arguments in `train.py`.

## Error Handling

There is no explicit `try`/`except` anywhere in either file. Failure modes are
implicit and surface as standard Python/PyTorch/pandas exceptions:

- Missing/malformed CSVs → `FileNotFoundError` or a pandas parsing error from `pd.read_csv`.
- Non-numeric feature columns → error from `torch.tensor(X_df.values, dtype=torch.float32)`.
- Calling `predict` before `fit` → `AttributeError` (`self.root` is `None`, has no `is_leaf`).
- Empty `y` passed to `_gini` is handled explicitly (`return 0.0` if `y.numel() == 0`), the one guarded edge case in the module.

## Test Coverage

No test suite is present in this module (no `tests/`, `*_test.py`, or
`__tests__` directory found alongside `decision_tree.py` / `train.py`).
Correctness is currently only exercised implicitly by running `train.py`
against the bundled 14-row "Play Tennis" dataset and eyeballing the printed
tree and training accuracy.

### Known coverage gaps

- No unit tests for `_gini`, `_best_split`, `_majority_class`, or the stopping
  conditions in `_build_tree` in isolation.
- No test for `predict` on unseen/held-out data — `train.py` only reports
  training accuracy on the same rows used to fit the tree.
- No test for edge cases such as all-identical feature columns, ties in
  Gini gain, or continuous (non-categorical) feature columns.
- No regression test pinning the exact learned tree structure for the
  bundled dataset.

## Future Improvements

- Add a held-out `X_test.csv` / `y_test.csv` and report test (not just
  training) accuracy — noted directly in the previous README as a known gap.
- Add pruning/regularization guidance beyond manually tuning `max_depth` and
  `min_samples_split`.
- Add a unit test suite covering `_gini`, `_best_split`, and the stopping
  conditions in `_build_tree`.
- Support loading CSV paths via CLI args/config instead of hardcoded
  filenames in `train.py`.
