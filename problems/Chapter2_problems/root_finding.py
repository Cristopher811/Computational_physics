import sys
import math

def f(x):
    f = math.sin(x)
    return f

def bisection(f,xl,xr,nmax,tol):
    xm = (xl+xr)/2
    fl = f(xl)
    fr = f(xr)
    fm = f(xm)
    nfl = fl
    nfr = fr
    if fl*fr>0:
        sys.exit("root not bracketed")
    for i in range(nmax):
        if xr-xl<tol:
            sys.exit("root not bracketed")
        if fl*fr>0:
            sys.exit("root not bracketed")
        if fl*fm>0:
            xl = xm
            nfl = fm
            nfr = fr
        fl = nfl
        fr = nfr
        xm = (xl+xr)/2
        fm = f(xm)
    return (xm,fm)



## Bisection Method
root = bisection(f, 0,math.pi/2,100,0.01)
print(root)

