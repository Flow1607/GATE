import numpy as np

# 1. Define matrix P and find its eigenvalues
P = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
w = np.linalg.eigvals(P)

# Option A: Trace equals sum of eigenvalues
opt_a = np.isclose(P.trace(), w.sum())
print(f"Option A (Trace == sum(w)): {opt_a}")

# Option B: P^T @ P equals identity matrix
opt_b = np.allclose(P.T @ P, np.eye(3))
print(f"Option B (P-Transpose @ P == I)   : {opt_b}")

# Option C: P is skew-symmetric (P^T == -P)
opt_c = np.allclose(P.T, -P)
print(f"Option C (P-Transpose == -P)      : {opt_c}")

# Option D: Absolute magnitude of all eigenvalues is 1
opt_d = np.allclose(np.abs(w), 1.0)
print(f"Option D (|w| == 1)       : {opt_d}")

