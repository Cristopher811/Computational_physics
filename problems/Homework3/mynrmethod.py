import mpmath as mp
from mpmath import *
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
#        if(x0 == mp.pi):
#            break
        x0 = x
        value.append(x0)
        ite.append(nn)
    x = x0
    return ite,value


#n_ite = pi(22/7,10**3,1e-1200)[-1]
#value = pi(22/7,10**3,1e-1200)[1]
#
#l = len(value)-2

# calculate the order of convergence of the method 

#x_k = value[l]
#x_kp1 = value[l+1]
#x_km1 = value[l-1]
#x_km2 = value[l-2]
#  
#q = mp.log(mp.fabs((x_kp1-x_k)/(x_k-x_km1)))/mp.log(mp.fabs((x_k - x_km1)/(x_km1-x_km2)))
#print(q)
