import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([0.5, 1.0, 1.5])

matmul = a @ b
print("Dot Product:\n",matmul)


u = np.array([1.0, 0.0])
v = np.array([0.0, 1.0])
cosine_similarity = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

print("\ncos(u, v):\n", cosine_similarity)