#By Jaideep
# 23/09/26
import numpy as np

k = float(input("Enter k: "))
A = np.array([[1, 0, 1], #defining the question matrix 
              [0, k, 0],
              [3, 0, -1]])
eigs = np.sort(np.linalg.eigvals(A)) #np.linalg.eigvals produces eigen values of a matrix

print("Eigenvalues:", eigs) #printing the new eigen values
print("Matches [-2, 1, 2]:", np.allclose(eigs, [-2, 1, 2])) #matching with given eigen values 
