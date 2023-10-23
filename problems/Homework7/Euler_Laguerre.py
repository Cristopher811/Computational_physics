import numpy as np
import mpmath as mp
from mpmath import *
from sympy import *

mp.dps = 100; mp.pretty = True

def laguerre_weigths_roots(n,dgt):
    x = Symbol('x')
    roots = Poly(laguerre(n,x),x).all_roots()
    x_i = [rt.evalf(dgt) for rt in roots]
    w_i = [(rt/((n+1)*laguerre(n+1,rt))**2).evalf(dgt) for rt in roots]
    return x_i, w_i

def f(x):
    return mp.fmul(mp.exp(-x),mp.ln(x))
def g(x):
    return mp.fdiv(mp.sin(x),x)

n= 61 # number of points
dgt = 10 # digits
gl = laguerre_weigths_roots(n,dgt)
ngl = np.array(gl,dtype = object)

integral = 0
for i in range(n):
    integral += g(ngl[0][i])*ngl[1][i]*mp.exp(ngl[0][i])

print(integral)
