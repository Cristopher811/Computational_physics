import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from scipy.interpolate import barycentric_interpolate
x = np.arange(0,10)
y = np.sin(x)
f = interpolate.interp1d(x,y)
xnew = np.arange(0,9,0.1)
ynew = f(xnew)


x1 = np.linspace(0.0,10.0,11)
y1 = np.sin(x1)

x2 = np.linspace(min(x1),max(x1), num=100)
y2 = interpolate.barycentric_interpolate(x1,y1,x2)


plt.plot(x1,y1,'o')
plt.plot(x2,y2)
plt.plot(x,y,'o',xnew,ynew,'-')
plt.show()
