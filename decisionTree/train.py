"""
train.py
=========

Loads the training data from `X_train.csv` and `y_train.csv` with pandas,
trains the PyTorch-based `DecisionTreeClassifier` from `decision_tree.py`,
prints the resulting tree structure, and reports training accuracy.

Usage
-----
    python train.py
"""

import pandas as pd
import torch

from decision_tree import DecisionTreeClassifier

# ----------------------------------------------------------------------
# 1. Load the data with pandas.
#    - X_train.csv holds the input features, one row per training
#      example, already encoded as integers (see README.md for the
#      encoding table).
#    - y_train.csv holds the single target column, one row per example,
#      aligned by row order with X_train.csv.
# ----------------------------------------------------------------------
X_df = pd.read_csv("X_train.csv")
y_df = pd.read_csv("y_train.csv")

feature_names = list(X_df.columns)
target_name = y_df.columns[0]

print(f"Loaded {len(X_df)} training examples.")
print(f"Features: {feature_names}")
print(f"Target:   {target_name}\n")

# ----------------------------------------------------------------------
# 2. Convert the pandas DataFrames into PyTorch tensors.
#    - X: float32 tensor of shape (n_samples, n_features)
#    - y: long (int64) tensor of shape (n_samples,) since class labels
#      are discrete category indices, not continuous values.
# ----------------------------------------------------------------------
X_train = torch.tensor(X_df.values, dtype=torch.float32)
y_train = torch.tensor(y_df[target_name].values, dtype=torch.long)

# ----------------------------------------------------------------------
# 3. Train the decision tree.
#    max_depth and min_samples_split are kept small on purpose: this toy
#    dataset only has 14 rows, so a deep tree would just memorize noise.
# ----------------------------------------------------------------------
tree = DecisionTreeClassifier(max_depth=4, min_samples_split=2)
tree.fit(X_train, y_train)

print("Learned tree structure:")
tree.print_tree(feature_names=feature_names)
print()

# ----------------------------------------------------------------------
# 4. Evaluate on the training set itself (this toy example has no
#    separate test set - see README.md for how to extend this).
# ----------------------------------------------------------------------
predictions = tree.predict(X_train)
accuracy = (predictions == y_train).float().mean().item()

print(f"Training accuracy: {accuracy * 100:.2f}%")
