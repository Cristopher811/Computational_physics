import numpy as np
from scipy.linalg import lu

############### LU Decomposition ###############

# Example matrix

A = np.array([[1,1,1],[1,1,1],[1,1,1]])

# Perform the LU decomposition

P,L,U = lu(A)

# Print the results
print("Matrix A:")
print(A)
print("\nPermutation matrix P:")
print(P)
print("\nLower triangular matrix L:")
print(L)
print("\nUpper triangular matrix U:")
print(U)


############## Sparse Matrix ###############

from scipy.sparse import csr_matrix
import random

# Create a large dense matrix

n=100
dense_matrix = np.zeros((n,n)) # nxn matrix filled with zeros

nonzero = n
for i in range(nonzero):
    n1 = random.randint(0,n-1)
    n2 = random.randint(0,n-1)
    dense_matrix[n1,n2] = random.uniform(-1,1)

# Convert the dense matrix to a sparse matrix

sparse_matrix = csr_matrix(dense_matrix)

dense_memory = dense_matrix.nbytes
sparse_memory = sparse_matrix.data.nbytes + sparse_matrix.indptr.nbytes + sparse_matrix.indices.nbytes

print(f"Memory usage of dense matrix: {dense_memory} bytes")
print(f"Memory usage of sparse matrix: {sparse_memory} bytes")

# Calculate the eigenvalues and eigenvectors of the sparse matrix

import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh
from numpy.linalg import eig

w,v = eig(dense_matrix)
print("Eigenvalues:",w)
print("Eigenvectors:",v)
w,v = eigsh(sparse_matrix)
print("Eigenvalues:",w)
print("Eigenvectors:",v)

plt.imshow(dense_matrix,cmap='viridis',interpolation='nearest')
plt.colorbar()
plt.show()


