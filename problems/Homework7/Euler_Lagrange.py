import numpy as np
import mpmath as mp
from mpmath import *
from sympy import *

mp.dps = 40; mp.pretty = True

# define the legendre weights and roots

def legendre_weights_roots(n,dgt):
    x = Symbol('x')
    roots = Poly(legendre(n,x),x).all_roots()
    x_i = [rt.evalf(dgt) for rt in roots]
    w_i = [(2*(1-rt**2)/(n+1)**2/(-rt*legendre(n, rt)+ legendre(n+1,rt))**2).evalf(dgt) for rt in roots]
    return x_i, w_i

def f(x): #function to integrate
    x2 = mp.fmul(-x,x)
    return mp.exp(x2)

def g(x): #function to integrate
    x2 = mp.fmul(x,x)
    return mp.sin(x)**2/x2

n=50 #number of points
dgt=50 #number of digits
gl=legendre_weights_roots(n,dgt) #legendre weights and roots

# calculates the integral numerically

integral = 0
for i in range(n):
    integral += g(gl[0][i])*gl[1][i] # change the the function you want to integrate

print(integral)
pi = mp.pi

print(pi-integral)








