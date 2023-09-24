import numpy as np
import matplotlib.pyplot as plt

def factorial(x):
    fac = 1
    for i in range(0,x-1):
        fac *= (x-i)
    return fac

def exp(x):
    return np.exp(x)

x = np.linspace(2,100,98)

ex = exp(x)
fac = factorial(x)

plt.plot(x,fac)
plt.plot(x,ex)
plt.show()
