import numpy as np
import matplotlib.pyplot as plt


# implement the euler method for the next equation:

def equation(y):
    rhs = y**2+1
    return rhs

def euler(y0, h, iterations):
    y = np.zeros(iterations)
    y[0] = y0
    for i in range(1,iterations):
        y[i] = y[i-1] + equation(y[i-1])*h
    return y

y0 = 0
h = 0.001
iterations = 100

y = euler(y0, h, iterations)
x = np.linspace(0,1,iterations)

plt.plot(x,y)
plt.show()




