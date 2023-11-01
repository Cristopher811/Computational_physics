# Cromer
import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation for the nonlinear pendulum
def nonlinear_pendulum(t, theta, omega, g, L):
    # Equations of motion
    theta_dot = omega
    omega_dot = g*np.sin(theta) / L
    return theta_dot, omega_dot

# Set the initial conditions
t0 = 0.0
theta0 = np.pi/2
omega0 = 0.0

# Set the time step size and the number of iterations
dt = 0.01
num_iterations = 10**3

g = 9.81  
L = 1.0   

# Initialize arrays to store the solution
t_values = np.zeros(num_iterations + 1)
theta_values = np.zeros(num_iterations + 1)
omega_values = np.zeros(num_iterations + 1)
energy_values = np.zeros(num_iterations + 1)

# Perform the Euler-Cromer method
t_values[0] = t0
theta_values[0] = theta0
omega_values[0] = omega0
energy_values[0] = 0.5 * L * omega0**2 - g * L * (1 - np.cos(theta0))

for i in range(num_iterations):
    t = t_values[i]
    theta = theta_values[i]
    omega = omega_values[i]
    theta_dot, omega_dot = nonlinear_pendulum(t, theta, omega, g, L)
    
    omega_new = omega + omega_dot * dt
    theta_new = theta + omega_new * dt
    
    t_values[i + 1] = t + dt
    theta_values[i + 1] = theta_new
    omega_values[i + 1] = omega_new
    
    # Calculate the energy at each step
    energy_values[i + 1] = 0.5 * L * omega_new**2 - g * L * (1 - np.cos(theta_new))

# Create subplots for Phase Space, Angle vs Time, and Energy vs Time
plt.figure(figsize=(14, 4))

# Phase Space
plt.subplot(1, 3, 1)
plt.title('Phase Space')
plt.plot(theta_values, omega_values)
plt.xlabel('Angle')
plt.ylabel('Angular Velocity')

# Angle vs Time
plt.subplot(1, 3, 2)
plt.title('Angle vs Time')
plt.plot(t_values, theta_values)
plt.xlabel('Time')
plt.ylabel('Angle')

# Energy vs Time
plt.subplot(1, 3, 3)
plt.title('Energy vs Time')
plt.plot(t_values, energy_values)
plt.xlabel('Time')
plt.ylabel('Energy')

plt.tight_layout()
plt.show()

