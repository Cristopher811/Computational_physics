import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.hermite as Herm
import math

#Choose simple units
m = 1
hbar = 1
w = 1

# discretized space
dx = 0.05
x_lim = 12
x = np.arange(-x_lim,x_lim,dx)

def hermite(x, n):
    xi = np.sqrt(m*w/hbar)*x
    herm_coeffs = np.zeros(n+1)
    herm_coeffs[n] = 1
    return Herm.hermval(xi, herm_coeffs)
  
def stationary_state(x,n):
    xi = np.sqrt(m*w/hbar)*x
    prefactor = 1./math.sqrt(2.**n * math.factorial(n)) * (m*w/(np.pi*hbar))**(0.25)
    psi = prefactor * np.exp(- xi**2 / 2) * hermite(x,n)
    return psi

plt.figure()
n = 5
for i in range(0,n):
    psi = stationary_state(x,i)
    energy = i + 0.5
    plt.plot(x,psi, label=f'$n={i}$, $E={energy}$')

plt.xlabel(r"x")
plt.ylabel(r"$\psi_n(x)$")
plt.title(r"Test Plot of $\psi_n(x)$")
plt.legend()
plt.show()
