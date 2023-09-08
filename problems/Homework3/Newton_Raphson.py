# defines the function
def f(x):
    f = x**3-x**2-x+1
    return f

def df(x):
    der = 3*x**2-2*x-1
    return der

#####################################################

def nr(x0,nmax,tol):
    x = x0
    if abs(df(x)) < tol:
        dx = 0
    else:
        dx = f(x)/df(x)
    for i in range(nmax):
        n = i
        if abs(dx) < tol:
            x0 = x -dx
            break
        x = x0-dx
        if abs(df(x)) < tol:
            dx = 0
        else:
            dx = f(x)/df(x)
        x0 = x
    x = x0
    return (x,f(x),n)



