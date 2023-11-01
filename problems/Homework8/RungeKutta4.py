# RungeKutta4
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
theta0 =  np.pi/2 # Initial angle 
omega0 = 0.0  # Initial angular velocity
energy0 = 0.5 * L * omega0**2 + g * (1 - np.cos(theta0))


# Time settings
t_max = 10  # Maximum time
h = 0.01  # Step size
num_steps = int(t_max / h)

# Initialize arrays 
t_values = np.zeros(num_steps + 1)
theta_values = np.zeros(num_steps + 1)
omega_values = np.zeros(num_steps + 1)

# Energy array to store the energy values
energy_values = np.zeros(num_steps + 1)
energy_values[0] = energy0
# Initial conditions
t_values[0] = t0
theta_values[0] = theta0
omega_values[0] = omega0

# Modify the angle to stay within [-pi, pi]
def enforce_periodicity(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi

def RungeKutta4(t, x, g, L):
# Solve the system using the Runge-Kutta method
    for i in range(num_steps):
        t = t_values[i]
        x = [enforce_periodicity(theta_values[i]), omega_values[i]]

        k1 = np.multiply(h, pendulum_system(t, x, g, L))
        k2 = np.multiply(h, pendulum_system(t + 0.5 * h, np.add(x, 0.5 * k1), g, L))
        k3 = np.multiply(h, pendulum_system(t + 0.5 * h, np.add(x, 0.5 * k2), g, L))
        k4 = np.multiply(h, pendulum_system(t + h, np.add(x, k3), g, L))
        x_new = np.add(x, (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        t_values[i + 1] = t + h

        theta_values[i + 1] = x_new[0]
        omega_values[i + 1] = x_new[1]

        # Calculate and store the energy at each step
        energy_values[i + 1] = 0.5 * L * omega_values[i + 1]**2 + g * (1 - np.cos(theta_values[i + 1]))

    return t_values, theta_values,omega_values,energy_values

t = []
theta = []
omega = []
energy = []
t,theta,omega,energy = RungeKutta4(t0, [theta0, omega0], g, L)

print(energy)

# Create subplots in a single line
plt.figure(figsize=(14, 4))
plt.subplot(1, 3, 1)
plt.title('Phase Space')
plt.plot(theta_values, omega_values)
plt.xlabel('Angle')
plt.ylabel('Angular Velocity')

plt.subplot(1, 3, 2)
plt.title('Angle vs Time')
plt.plot(t_values, theta_values)
plt.xlabel('Time')
plt.ylabel('Angle')

plt.subplot(1, 3, 3)
plt.title('Energy vs Time')
plt.plot(t_values,energy)
plt.xlabel('Time')
plt.ylabel('Energy')

plt.tight_layout()
plt.show()
