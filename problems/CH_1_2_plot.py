import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

x = np.linspace(-np.pi*2,np.pi*2,1000)
y = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x,y)

ax.set_ylabel('$\sin(x)$')
ax.set_xlabel('x')

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)


# Plot the surface
fig1, ax1 = plt.subplots(subplot_kw={"projection": "3d"})
ax1.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('$\sin{\sqrt{x^2+y^2}}$')

plt.show()




