import numpy as np
import matplotlib.pyplot as plt

def sch(y,xi,k):
    phi,dphi = y
    dydx = [dphi, (xi**2-k)*phi]
    return dydx

def evolve(L,k):
    phi0 = [0.0,1.0]
    xi = np.linspace(0,L,1000)
    from scipy.integrate import odeint
    sol = odeint(sch,phi0,xi,args = (k,))
    return sol

L= 5
#k =  # 9.000025350542273 # 5.000000213331077  # 0.999999959662091 # even bound_states
#k = # 7.000002433254849 # 2.9999999884166755  # odd bound_states
sol = evolve(L,k)
x = np.linspace(0,L,1000)

plt.ylim(-4,4)
plt.xlim(0,L)
plt.xlabel('xi')
plt.ylabel('$\psi(xi)$')
plt.grid()
plt.plot(x,sol[:,0])
plt.show()


