import numpy as np
import matplotlib.pyplot as plt

def equation(x, x_dot):
    k = 1
    b = 1
    V_prime = k*x +b*x**3
    return -V_prime

# Set the initial conditions
t0 = 0
x0 = 1
x_dot0 = 10

# Set the time step size and the number of iterations
dt = 0.00001
num_iterations = 10**3

# Initialize arrays to store the solution
t = np.zeros(num_iterations)
x = np.zeros(num_iterations)
x_dot = np.zeros(num_iterations)
e = np.zeros(num_iterations)

# Perform Euler-Cromer method
k=1
b=10
t[0] = t0
x[0] = x0
x_dot[0] = x_dot0
e[0] = (x_dot[0]**2)/2 + k*x[0]**2/2 + b*x[0]**4/4
for i in range(1, num_iterations):
    t[i] = t[i-1] + dt
    x_dot[i] = x_dot[i-1] + equation(x[i-1], x_dot[i-1])*dt
    x[i] = x[i-1] + x_dot[i]*dt
    e[i] = (x_dot[i]**2)/2 + k*x[i]**2/2 + b*x[i]**4/4


plt.plot(t,e)
plt.xlabel('t')
plt.ylabel('Energy')
plt.title('Mechanical energy')
plt.grid(True)
plt.show()


#Plot the results
plt.plot(x,x_dot)
plt.xlabel('x')
plt.ylabel('v')
plt.title('Euler method solution')
plt.grid(True)
plt.show()


