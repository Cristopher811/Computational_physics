import numpy as np
import matplotlib.pyplot as plt


#define schrodinger equation:

def sch(y,xi,k):
    phi,dphi = y
    dydx = [dphi, (xi**2-k)*phi]
    return dydx

def evolve(L,k):
    phi0 = [0.0,1.0]
    xi = np.linspace(0,L,501)
    from scipy.integrate import odeint
    sol = odeint(sch,phi0,xi,args = (k,))
    val = sol[:,0][[500]]
    return val[0]


L=5
kmin = 0.0
kmax = 10.0
nmax = 10**3
val1 = []
val2 = []
for j in range(nmax):
    k = kmin + (kmax-kmin)*j/(nmax-1)
    val2.append(np.log(abs(evolve(L,k))))    
    val1.append(k)


def f(eguess):
    f = evolve(L,eguess)
    return f

#bisection method to find root 
def bisection(f,xl,xr,tol):
    while (xr - xl) / 2.0 > tol:
        xm = (xl + xr) / 2.0
        if f(xm) == 0:
            return xm
        elif f(xl)*f(xm) < 0:
            xr = xm
        else:
            xl = xm
    return (xl + xr) / 2.0

xl = 6.0
xr = 8.0
tol = 1e-10
root = bisection(f,xl,xr,tol)
print(root)

plt.plot(val1,val2)
plt.show()



