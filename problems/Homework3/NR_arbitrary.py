import mpmath
from mpmath import *

mp.dps = 40; mp.pretty = True

#defines the function

def f(x):
    x2 = mpmath.fmul(x,x)
    x3 = mpmath.fmul(x,x2)
    p1 = mpmath.fadd(x3,1)
    p2 = mpmath.fsub(p1,x2)
    f = mpmath.fsub(p2,x)
    
    return f

# defines the derivative of the function

def df(x):
    x2 = mpmath.fmul(x,x) 
    p1 = mpmath.fmul(3,x2)
    p2 = mpmath.fmul(2,x)
    p3 = mpmath.fsub(p1,p2)
    der = mpmath.fsub(p3,1)
    return der 

##################################################

def nrmpmath(x0,nmax,tol):
    x = x0
    if mpmath.fabs(df(x))<tol:
        dx = 0
    else:
        dx = f(x)/df(x)
    for i in range(nmax):
        nn = i
        if mpmath.fabs(dx)<tol:
            x0 = x - dx
            break
        x = x0-dx
        if mpmath.fabs(df(x)) < tol:
            dx = 0
        else:
            dx = f(x)/df(x)
        x0 = x
    x = x0

    return(x,f(x),nn)


