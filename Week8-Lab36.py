import  numpy as np
import pandas as pd


#1) Create feature and weight vectors
feature = np.array([30.0, 50.0, 10.0])
weights = np.array([0.05, 0.8, -0.1])

#vector addition
f_w_sum = feature + weights
print("v_sum:", f_w_sum, "shape:", f_w_sum.shape)

#scalar multiplication
v_small = 0.1 * feature
v_neg = -2.0 * feature

#3) Compute norms and inspect shapes
print("\n||feature||:", np.linalg.norm(feature))
print("\n||weights||:", np.linalg.norm(weights))

print("feature shape:", feature.shape)
print("weights shape:", weights.shape)

