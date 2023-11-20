import numpy as np

N = 5

# Define a grid of points in the plane
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
coords = [[xi, yj] for xi in x for yj in y]

h = x[1] - x[0]

# Finite difference representation of the second derivative
der2 = (1/2 * h**2) * (np.diag(-1 * np.ones(N-1), k=-1) + np.diag(2 * np.ones(N), k=0) + np.diag(-1 * np.ones(N-1), k=1))

for i in range(1,(2*N-1)**2):
    kx[i] = 

