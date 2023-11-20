import numpy as np
from scipy.sparse import coo_matrix
import matplotlib.pyplot as plt

nmax = 2
h = 1 / (2 * nmax)

DATA = [(i, j) for i in range(-nmax + 1, nmax) for j in range(-nmax + 1, nmax)]

der2 = np.diag(-1 * np.ones(nmax - 1), k=-1) + np.diag(2 * np.ones(nmax), k=0) + np.diag(-1 * np.ones(nmax - 1), k=1)

KX = np.zeros((2 * nmax - 1) ** 2)
KY = np.zeros((2 * nmax - 1) ** 2)

for q in range((2 * nmax - 1) ** 2):
    KX[q] = DATA[q][0]
    KY[q] = DATA[q][1]

def kronecker_delta(ki, kj):
    return np.eye(len(ki))[ki, kj]

count = 0
vec = []

for r in range((2 * nmax - 1) ** 2):
    for q in range(r):
        mat = -der2[KX[q], KX[r]] * kronecker_delta(KY[q], KY[r]) - der2[KY[q], KY[r]] * kronecker_delta(KX[q], KX[r])
        if abs(mat) > 0:
            count += 1
            vec.append((q, r, mat))
            count += 1
            vec.append((r, q, mat))

for q in range((2 * nmax - 1) ** 2):
    mat = -der2[KX[q], KX[q]] * kronecker_delta(KY[q], KY[q]) - der2[KY[q], KY[q]] * kronecker_delta(KX[q], KX[q])
    if abs(mat) > 0:
        count += 1
        vec.append((q, q, mat))

row, col, data = zip(*vec)
MATRIX = (1 / (h ** 2)) * coo_matrix((data, (row, col)))

GRID = np.array([(KX[q] * h, KY[q] * h) for q in range((2 * nmax - 1) ** 2)])

result = [(2 * nmax - 1) ** 2, GRID, MATRIX]
print(MATRIX.toarray())

plt.imshow(MATRIX.toarray())
plt.colorbar()
plt.show()
