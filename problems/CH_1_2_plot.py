import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

x = np.linspace(-np.pi*2,np.pi*2,1000)
y = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x,y)

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface
fig1, ax1 = plt.subplots(subplot_kw={"projection": "3d"})
ax1.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

ax1.set(xticklabels=[X],
       yticklabels=[Y],
       zticklabels=[Z])



plt.show()




