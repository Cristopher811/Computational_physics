import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation
def equation(x, x_dot):
    V_prime = -x**2 + 2  
    kappa = 1
    return V_prime - kappa*x_dot

# Set the initial conditions
t0 = 0
x0 = 2
x_dot0 = 0

# Set the time step size and the number of iterations
dt = 0.01
num_iterations = 10**4

# Initialize arrays to store the solution
t = np.zeros(num_iterations)
x = np.zeros(num_iterations)
x_dot = np.zeros(num_iterations)

# Perform Euler's method
t[0] = t0
x[0] = x0
x_dot[0] = x_dot0
for i in range(1, num_iterations):
    t[i] = t[i-1] + dt
    x_dot[i] = x_dot[i-1] + equation(x[i-1], x_dot[i-1])*dt
    x[i] = x[i-1] + x_dot[i-1]*dt

# Approximate the value of sqrt(2)
approx_sqrt2 = x[-1]
print(x_dot[-1])
print("Approximation of sqrt(2):", approx_sqrt2)


# Plot the mechanical energy
energy = (x_dot**2)/2 - (x**3)/3 + 2*x

plt.plot(t, energy)
plt.xlabel('t')
plt.ylabel('Energy')
plt.title('Mechanical energy')
plt.grid(True)
plt.show()


#Plot the results
#plt.plot(x,x_dot)
#plt.xlabel('x')
#plt.ylabel('v')
#plt.title('Euler method solution')
#plt.grid(True)
#plt.show()


