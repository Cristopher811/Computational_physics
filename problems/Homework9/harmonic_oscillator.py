import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar
from scipy.special import hermite

N = 2000
hbar = 1
omega = 1
m = 1

def construct_hamiltonian(N, hbar, m, omega):
    # defining the grid
    x = np.linspace(-10,10,N)
    y = np.linspace(-10,10,N)
    # find the spacing between the grid
    h = x[1] - x[0]

    kinetic_energy_matrix = (1/h**2)*(hbar**2/2*m)*(np.diag(-1*np.ones(N-1), k=-1) + np.diag(2*np.ones(N),k=0) + np.diag(-1*np.ones(N-1), k=1))
    harmonic_potential_matrix = np.diag((0.5*m*omega**2*(x**2+y**2))*np.ones(N))
    hamiltonian_matrix = harmonic_potential_matrix + kinetic_energy_matrix
    eigenvalues,eigenvectors = np.linalg.eigh(hamiltonian_matrix)
    
    return eigenvalues,eigenvectors

eigenvalues,eigenvectors = construct_hamiltonian(N, hbar, m, omega)

x_values = np.linspace(-1, 1, N)  

normalized_eigenvectors = eigenvectors/np.linalg.norm(eigenvectors,axis=0)

plt.plot(x_values,-1*normalized_eigenvectors[:,0],label='Numerical (adjusted)')
plt.title('Harmonic Oscillator Eigenfunctions')
plt.xlabel('x')
plt.ylabel('Wave function')
plt.legend()
plt.grid(True)
plt.show()

eigenvalues_list = list(eigenvalues[1:20])

n = np.linspace(1,19,19)

analytic_eigenvalue = [hbar * omega * (0.5 + k) for k in n]

print(eigenvalues_list,analytic_eigenvalue)

plt.figure(figsize=(8, 4))
plt.scatter(n,eigenvalues_list,label='Numerical eigenvalues')
plt.scatter(n,analytic_eigenvalue,color='red',label='Analytic eigenvalues')
plt.xlabel('n')
plt.ylabel('Eigenvalues')
plt.legend()
plt.xticks(np.arange(1, 20, step=1))
plt.show()
