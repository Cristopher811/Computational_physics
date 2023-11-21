import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

def LAPLA2D(n0):
    nmax = n0

    h = 1/2/nmax

    DATA = [(i, j) for i in range(-nmax + 1, nmax) for j in range(-nmax + 1, nmax)]

    def der2(k, l):
        h = 1/2/nmax
        if k == l + 1 or k == l - 1:
            return 1 / h**2
        elif k == l:
            return -2 / h**2
        else:
            return 0


    # Initializing KX and KY arrays
    KX = [0]*((2 * nmax - 1)**2)
    KY = [0]*((2 * nmax - 1)**2)

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
            mat = -der2(KX[q],KX[r]) * kronecker_delta(KY[q], KY[r]) - der2(KY[q],KY[r]) * kronecker_delta(KX[q], KX[r])
            if abs(mat) > 0:
                count += 1
                vec.append((q, r, mat))
                count += 1
                vec.append((r, q, mat))

    # Loop to handle diagonal elements
    for q in range(0, (2 * nmax - 1)**2):
        mat = -der2(KX[q],KX[q]) * kronecker_delta(KY[q], KY[q]) - der2(KY[q],KY[q]) * kronecker_delta(KX[q], KX[q])
        if abs(mat) > 0:
            count += 1
            vec.append((q, q, mat))

    row, col, data = zip(*vec)
    MATRIX = coo_matrix((data, (row, col)))

    # Build the GRID array
    GRID = np.array([(KX[q] * h, KY[q] * h) for q in range(0, (2 * nmax - 1)**2)])

    result = [(2 * nmax - 1)**2, GRID, MATRIX]

    return result

# Initialize variables
#n0_values = []
#NH_values = []
#EG_values = []

# Loop to calculate eigenvalues
#for k in range(0,14):
#    n0 = 5 + (k - 1)
#    n0_values.append(n0)
#    NH_values.append(1 / (2 * n0))
#
#    # Calculate Laplacian matrix using LAPLA2D function
#    laplacian_matrix = LAPLA2D(n0)
#
#    # Compute eigenvalues using eigsh
#    eigenvalues, _ = eigsh(laplacian_matrix, k=1, which='SA', maxiter=40)
#
#    EG_values.append(eigenvalues[0])
#
#    print(f"{k} {eigenvalues[0]}")

# numerical results

nmax = 5
L = 1
h = 1/2/nmax
DATA = LAPLA2D(nmax)

plt.imshow(DATA[2].toarray())
plt.show()


def xx(k,nn,l):
    return k/nn*l/2

_,EGVEC = eigsh(DATA[2], k=100, which='SA', maxiter=40)

EGVECord = {}

# Ordering the eigenvectors
for j in range(100):
    EGVECord[j + 1] = EGVEC[:, j]


# Compute eigenvalues using eigsh
eigenvalues, _ = eigsh(DATA[2], k=100, which='SA')

# Order the eigenvalues in ascending order
EGVAL = np.sort(eigenvalues)

def tent(k, NN, L, x):
    if x <= xx(k - 1, NN, L) and x >= xx(k, NN, L):
        return (x - xx(k - 1, NN, L)) / (xx(k, NN, L) - xx(k - 1, NN, L))
    elif x > xx(k, NN, L) and x <= xx(k + 1, NN, L):
        return (xx(k + 1, NN, L) - x) / (xx(k + 1, NN, L) - xx(k, NN, L))
    else:
        return 0


# n0 specifies which eigenfunction is being considered
n0 = 100

# CWF function definition
def CWF(x, y):
    return np.sum(
        EGVECord[n0][p - 1] *
        tent(DATA[1][p - 1][0] / h, nmax, L, x) *
        tent(DATA[1][p - 1][1] / h, nmax, L, y)
        for p in range(1, DATA[0] + 1)
    )/(L / 2 / nmax)

# Piecewise potential function
#def V(x, y, L):
#    return np.piecewise(x, [np.abs(x) >= L, np.abs(y) >= L], [1, 0])

# Generate grid points
x_vals = np.linspace(-L/2, L/2, 100)
y_vals = np.linspace(-L/2, L/2, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Evaluate CWF and V on the grid
Z_CWF = np.vectorize(CWF)(X, Y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z_CWF, cmap='rainbow')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
