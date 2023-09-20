import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 
import sys

# define schrödinger equation
def sch(y, x, beta, epsilon):
    phi, dphi = y
    dydx = [dphi, -1./(1. + (beta*x/10)**2)*phi - epsilon*phi]
    return dydx

def numsol(L,beta,epsilon):
    phi0 = [0.0,1.0] #initial condition for phi(y)
    x = np.linspace(0,L,1000)
    sol = odeint(sch, phi0, x, args=(beta, epsilon))
    return sol

L = 20
beta = 1
#epsilon = #-0.3672235061178116 #-0.3676931 # -0.5893558163661508 # -0.906983436504379  even bound_states
epsilon = -0.4678218032831767 # -0.7348752335762829
sol = numsol(L,beta,epsilon)

x = np.linspace(0,L,1000)

plt.plot(x,sol[:,0])
plt.xlim(0,L)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$\phi(x)$')
plt.show()
