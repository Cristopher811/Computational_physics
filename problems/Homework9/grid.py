import numpy as np
import matplotlib.pyplot as plt

N = 5

# Define a grid of points in the plane
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
coords = [[xi, yj]  for xi in x for yj in y]

h = x[1] - x[0]

der2 = (1/2*h**2)*(np.diag(-1*np.ones(N-1), k=-1) + np.diag(2*np.ones(N),k=0) + np.diag(-1*np.ones(N-1), k=1))

kx = np.arange((2*N-1)**2)
ky = np.arange((2*N-1)**2)

def kronecker_delta(ki,kj):
    return 1 if ki == kj else 0

count = 0
vec = []

for i in range(2*N-1):
    for j in range(2*N-1):
        q = i*(2*N-1) + j
        for r in range(q):
            mat = -1 * der2[kx[q]][kx[r]] * kronecker_delta(ky[q], ky[r]) - 1 * der2[ky[q]][ky[r]] * kronecker_delta(kx[q], kx[r])
            if abs(mat) > 0:
                count += 1
                vec.append([q,r,mat])
                count += 1
                vec.append([r,q,mat])


for q in range((2*N-1)**2):
    mat = -1*der2[kx[q]][kx[q]] * kronecker_delta(ky[q], ky[q]) - 1 * der2[ky[q]][ky[q]] * kronecker_delta(kx[q], kx[q])
    if abs(mat) > 0:
        count += 1
        vec.append([q,q,mat])

MATRIX = np.zeros(((2*N-1)**2,(2*N-1)**2))
for j in range(count):
    MATRIX[vec[j][0]][vec[j][1]] = vec[j][2]

GRID = np.array([[kx[q] * h, ky[q] * h] for q in range((2 * N - 1)**2)])

# Print or use MATRIX and GRID as needed
print("MATRIX:")
print(MATRIX)
print("\nGRID:")
print(GRID)


#kx = []
#ky = []
#
## put the index of each element in the list
#for i in range((2*N-1)**2):
#    kx.append(i)
#    ky.append(i)
#
#
#
#def kronecker_delta(ki,kj):
#    if ki == kj:
#        return 1
#    else:
#        return 0
#
#count = 0
#
#for i in range(N):
#    for j in range(N):
#        mat = -1*der2[kx[i]][kx[j]]*kronecker_delta(ky[i], ky[j]) - 1*der2[ky[i]][ky[j]]*kronecker_delta(kx[i], kx[j])
