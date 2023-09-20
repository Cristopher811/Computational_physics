from scipy.optimize import minimize_scalar


def f(x):
    return (x+1)**2

print('Using minimize scalar, without specifying method')
sol = minimize_scalar(f)
print(sol.x)

print('Using minimize scalar, specifying method Brent')
sol = minimize_scalar(f, method='Brent')
print(sol.x)


print('Using minimize scalar, using method bounded')
sol = minimize_scalar(f,bounds = (0,1), method='bounded')
print(sol.x)


from scipy.optimize import minimize, rosen, rosen_der

#initial point

x0 = [1.3,0.7,0.8,1.9,1.2]

val_in = rosen(x0)
print('Value at the initial point = ',val_in)

res = minimize(rosen,x0,method='Nelder-Mead',tol = 1e-6)

val_fin = rosen(res.x)
print('value at the final point = ', val_fin)


res = minimize(rosen,x0,method='Newton-CG',jac = rosen_der,tol = 1e-6)
val_fin = rosen(res.x)

print('Vale at the final point = ', val_fin)
