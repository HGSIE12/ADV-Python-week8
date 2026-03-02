import numpy as np

X = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])
W = np.array([
    [0.1, -0.2],
    [0.4, 0.0],
    [-0.3, 0.5],
])

print("X shape: ", X.shape) # (3, 3)
print("\nW shape: ", W.shape) # (3, 2)


res = np.dot(X, W)
print("\nres shape: ", res.shape) #(2, 2)


X_T = X.T # (3, 2)
print("X shape:", X.shape, "X_T shape:", X_T.shape)
