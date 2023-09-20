import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 

# define schrödinger equation
def sch(y, x, beta, epsilon):
    phi, dphi = y
    dydx = [dphi, -1./(1. + (beta*x/10)**2)*phi - epsilon*phi]
    return dydx

# evolve the schrödinger equation
def evolve(L, beta, epsilon):
    phi0 = [0.0,1.0] #initial condition for phi(y)
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
    val2.append(np.log(abs(evolve(L,beta,epsilon))))    #(np.log(abs(evolve(L,beta,epsilon))))
    val1.append(epsilon)


#defines the function
def f(eguess):
    f = evolve(L,beta,eguess)
    return f

#implements the bisection method
def bisection(x0,xf,nmax,tol):
    xm = 0
    for i in range(nmax):
        f0 = f(x0)
        xm = (x0 + xf) / 2.0
        fm = f(xm)
        if f(xf)*f(x0) > 0:
            return None
        if fm == 0 or abs(x0 - xf) < tol:
            break
        if f0*fm < 0:
            xf = xm
        else:
            x0 = xm
    return xm


tol = 1e-100
xl = -0.2
xr = 0.0

root = bisection(xl,xr,1000,tol)
print(root)

plt.plot(val1,val2)
plt.xlabel('$\epsilon$')
plt.ylabel('$\log(|\phi(20)|)$')
plt.show()


