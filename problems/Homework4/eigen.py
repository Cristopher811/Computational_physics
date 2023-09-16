import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

N = 2000
dy = 1/N
y = np.linspace(0, 1, N+1)

def ml2V(y):
    return -1/(1+y**2)

d = 1/dy**2 + ml2V(y)[1:-1]
e = -1/(2*dy**2) * np.ones(len(d)-1)

w,v = eigh_tridiagonal(d,e)

# plot the first for v's

plt.plot(v.T[0])
plt.plot(v.T[1])
plt.plot(v.T[2])
plt.plot(v.T[3])
#print(w[0:10].T)
#plt.bar(np.arange(0,10,1),w[0:10])
plt.show()




