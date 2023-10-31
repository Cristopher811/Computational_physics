import numpy as np
import matplotlib.pyplot as plt

# Define the system of ODEs
def pendulum_system(t, x, g, L):
    theta, omega = x
    theta_prime = omega
    omega_prime = -(g / L) * np.sin(theta)
    return [theta_prime, omega_prime]

# Parameters
g = 9.8
L = 1.0
t0 = 0.0
theta0 = np.pi  # Initial angle 
omega0 = 0.1  # Initial angular velocity

# Time settings
t_max = 10  # Maximum time
h = 0.01  # Step size
num_steps = int(t_max / h)

# Initialize arrays 
t_values = np.zeros(num_steps + 1)
theta_values = np.zeros(num_steps + 1)
omega_values = np.zeros(num_steps + 1)

# Initial conditions
t_values[0] = t0
theta_values[0] = theta0
omega_values[0] = omega0

def RungeKutta4(t, x, g, L):
# Solve the system using the Runge-Kutta method
    for i in range(num_steps):
        t = t_values[i]
        x = [theta_values[i], omega_values[i]]
        # how much numerical error we carry by multiplying by the step size?
        k1 = np.multiply(h, pendulum_system(t, x, g, L))
        k2 = np.multiply(h, pendulum_system(t + 0.5 * h, np.add(x, 0.5 * k1), g, L))
        k3 = np.multiply(h, pendulum_system(t + 0.5 * h, np.add(x, 0.5 * k2), g, L))
        k4 = np.multiply(h, pendulum_system(t + h, np.add(x, k3), g, L))
        x_new = np.add(x, (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        t_values[i + 1] = t + h
        theta_values[i + 1] = x_new[0]
        omega_values[i + 1] = x_new[1]

    return t_values, theta_values,omega_values

t = []
theta = []
omega = []
t,theta,omega = RungeKutta4(t0, [theta0, omega0], g, L)

# Plot the phase space
plt.figure(figsize=(8, 6))
plt.title('Phase Space')
plt.plot(theta, omega)
plt.xlabel('Angle')
plt.ylabel('Angular Velocity')

# Plot angle vs time
#plt.figure(figsize=(8, 6))
#plt.title('Angle vs Time')
#plt.plot(t, theta)
#plt.xlabel('Time')
#plt.ylabel('Angle')


plt.grid(True)
plt.show()

