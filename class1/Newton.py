import numpy as np
def f(x,y,z):
    return [x**2-z**2+1, y**2-z-1, z**2-y**2+z+x]

def df(x,y,z):
    return [[2*x, 0.,-2*z],[0,2*y,-1.],[1,-2*y,2*z+1]]

#number of iterations
iter = 5

p=np.array([2.,1.,0.1])
for i in range(iter):
    F = np.array(f(p[0],p[1],p[2]))
    A = np.array(df(p[0],p[1],p[2]))
    inv = np.linalg.inv(A)
    p2 = p-inv.dot(F)
    p = p2

print(p)
