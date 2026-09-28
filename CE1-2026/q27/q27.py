import numpy as np

# Define the matrix
A = np.array([[9, 15], [15, 50]])

# Perform Cholesky decomposition: A = L @ L.T
L = np.linalg.cholesky(A)

# Extract l_22 
l_22 = L[1, 1] #index 1 for row and column
abs_l_22 = int(np.abs(l_22))

print("Lower triangular matrix L:")
print(L)
print(f"\n|l_22| = {abs_l_22}")

