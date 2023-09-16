import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 
import sys

# define schrödinger equation
def sch(y, x, beta, epsilon):
    phi, dphi = y
    dydx = [dphi, -1./(1. + (beta*x/10)**2)*phi - epsilon*phi]
    return dydx

# evolve the schrödinger equation
def evolve(L, beta, epsilon):
    phi0 = [1,0.0] #initial condition for phi(y)
    x = np.linspace(0,L,501)
    from scipy.integrate import odeint
    sol = odeint(sch, phi0, x, args=(beta, epsilon))
    val = sol[:, 0][[500]]
    return val[0]

L=20
beta=1
epsmin = -1.0
epsmax = 0.0
nmax = 10**3
val1 = []
val2 = []
for j in range(nmax):
    epsilon = epsmin + (epsmax-epsmin)*j/(nmax-1)
    val2.append(np.log(abs(evolve(L,beta,epsilon))))
    val1.append(epsilon)


#defines the function
def f(eguess):
    f = evolve(L,beta,eguess)
    return f

#implements the bisection method
def bisection(f, xl, xr, tol):
    while (xr - xl) / 2.0 > tol:
        xm = (xl + xr) / 2.0
        if f(xm) == 0:
            return xm
        elif f(xl)*f(xm) < 0:
            xr = xm
        else:
            xl = xm
    return (xl + xr) / 2.0


xl = -1.0
xr = -0.8
tol = 1e-6

root = bisection(f,xl,xr,tol) #it works!! :)
print(root)

plt.plot(val1,val2)
plt.show()


