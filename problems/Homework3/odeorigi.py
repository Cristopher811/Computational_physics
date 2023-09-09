import numpy as np

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
