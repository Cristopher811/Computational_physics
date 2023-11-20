import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt

nmax = 2
h = 1/2/nmax

DATA = [(i, j) for i in range(-nmax + 1, nmax) for j in range(-nmax + 1, nmax)]

der2 = (1/2/h**2)*(np.diag(-1*np.ones(nmax-1), k=-1) + np.diag(2*np.ones(nmax),k=0) + np.diag(-1*np.ones(nmax-1), k=1))
print(der2)

# Initializing KX and KY arrays
KX = [0] * ((2 * nmax - 1)**2)
KY = [0] * ((2 * nmax - 1)**2)

# Associating a single index to each grid point
for q in range(0, (2 * nmax - 1)**2):
    KX[q] = DATA[q][0]
    KY[q] = DATA[q][1]

def kronecker_delta(ki,kj):
    if ki == kj:
        return 1
    else:
        return 0

count = 0
vec = []

# Loop to calculate matrix elements and populate vec
for r in range(0, (2 * nmax - 1)**2):
    for q in range(0, r):
        mat = -der2[KX[q],KX[r]] * kronecker_delta(KY[q], KY[r]) - der2[KY[q], KY[r]] * kronecker_delta(KX[q], KX[r])
        if abs(mat) > 0:
            count += 1
            vec.append((q, r, mat))  # Adjust indices here
            count += 1
            vec.append((r, q, mat))  # Adjust indices here

# Loop to handle diagonal elements
for q in range(1, (2 * nmax - 1)**2):
    mat = -der2[KX[q], KX[q]] * kronecker_delta(KY[q], KY[q]) - der2[KY[q], KY[q]] * kronecker_delta(KX[q], KX[q])
    if abs(mat) > 0:
        count += 1
        vec.append((q, q, mat))  # Adjust indices here

row, col, data = zip(*vec)
MATRIX = coo_matrix((data, (row, col))).toarray()

# Build the GRID array
GRID = np.array([(KX[q] * h, KY[q] * h) for q in range(0, (2 * nmax - 1)**2)])

result = [(2 * nmax - 1)**2, GRID, MATRIX]
print(MATRIX)

plt.imshow(MATRIX)
plt.colorbar()
plt.show()

