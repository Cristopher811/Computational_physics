import numpy as np
import matplotlib.pyplot as plt

def ode(y, t, b, c):
    x, dx = y
    dydt = [dx, 2-x**2-c*dx]
    return dydt


b = 0
c = 1
y0 = [2.0, 0.0]
t = np.linspace(0, 100, 501)
from scipy.integrate import odeint
sol = odeint(ode, y0, t, args=(b, c))

# Calculate the mechanical energy
v = sol[:,1]
x = sol[:,0] 

energy = (v**2)/2 - (x**3)/3 + 2*x

# plot the mechanical energy of the system

#plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, energy, label='Mechanica Energy')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
