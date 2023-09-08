import mpmath as mp
from mpmath import *
import matplotlib.pyplot as plt
mp.dps = 1200; mp.pretty = True

# Context from Function problems/Homework3/pidigits.py:df
def f(x):
    f = mp.sin(x)
    return f

def df(x):
    df = mp.cos(x)
    return df

#create a function that gives you an aproximation of pi using the Newton-Raphson method
def pi(x0,nmax,tol):
    value = []
    ite = []
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
        value.append(x0)
        ite.append(nn)
    x = x0
    return ite,value
