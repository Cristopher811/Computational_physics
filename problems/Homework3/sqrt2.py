import mpmath as mp
from mpmath import *
import numpy as np

mp.dps = 100; mp.pretty = True;

# construct a function using mpmath whose roots is the square root of 2
def f(x):
    x1 = mp.fmul(x,x)
    f = mp.fsub(x1,2)
    return f

def df(x):
    df = mp.fmul(x,2)
    return df

# Newton-Raphson method to find the roots of f(x):
def nr(x0,nmax,tol):
    x = x0
    if mp.fabs(df(x))<tol:
        dx = 0
    else:
        dx = f(x)/df(x)
    for i in range(nmax):
        nn = i
        if mp.fabs(dx)<tol:
            x0 = x - dx
            break
        x = x0-dx
        if mp.fabs(df(x)) < tol:
            dx = 0
        else:
            dx = f(x)/df(x)
        x0 = x
    x = x0
    return (x,f(x),nn)

root = nr(2,100,1e-100)
print(root)

difference = mp.fabs(root[0] -mp.sqrt(2))
print(difference)
