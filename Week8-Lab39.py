import numpy as np

X = np.array([
    [3.0, 4.0],
    [1.0, 2.0],
    [0.0, 5.0],
])

row_norms = np.linalg.norm(X, axis=1, keepdims=True)

X_normalized = X / row_norms

new_norms = np.linalg.norm(X_normalized, axis=1)

print("Row norms before normalization:\n", row_norms.flatten())
print("\nNormalized matrix:\n", X_normalized)
print("\nRow norms after normalization:\n", new_norms)