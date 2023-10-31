import numpy as np
import matplotlib.pyplot as plt

def pendulum_system(t, x, g, L):
    theta, omega = x
    theta_prime = omega
    omega_prime = -(g / L) * np.sin(theta)
    return np.array([theta_prime, omega_prime])

def runge_kutta_fehlberg(f, t, y, h, g, L):
    k1 = f(t, y, g, L)
    k2 = f(t + 0.25*h, y + 0.25*h*k1, g, L)
    k3 = f(t + 3*h/8, y + 3*h*k1/32 + 9*h*k2/32, g, L)
    k4 = f(t + 12*h/13, y + 1932*h*k1/2197 - 7200*h*k2/2197 + 7296*h*k3/2197, g, L)
    k5 = f(t + h, y + 439*h*k1/216 - 8*h*k2 + 3680*h*k3/513 - 845*h*k4/4104, g, L)
    k6 = f(t + 0.5*h, y - 8*h*k1/27 + 2*h*k2 - 3544*h*k3/2565 + 1859*h*k4/4104 - 11*h*k5/40, g, L)

    x_next = y + h*(25*k1/216 + 1408*k3/2565 + 2197*k4 /4104 - k5/5)
    y_next = y + h*(16*k1/135 + 6656*k3/12825 + 28561*k4/56430 - 9*k5/50 + 2*k6/55)

    return t + h, y_next, x_next

# Parameters
g = 9.81  # Acceleration due to gravity (m/s^2)
L = 1.0   # Length of the pendulum (m)
t0 = 0.0  # Initial time
theta0 = np.pi  # Initial angle 
omega0 = 0.1  # Initial angular velocity

# Time settings
t_max = 10.0  # Maximum time
h0 = 0.01  # Initial step size
t, y, x = t0, np.array([theta0, omega0]), np.array([theta0, omega0])

# Initialize arrays to store results
t_values = [t]
theta_values = [y[0]]
omega_values = [y[1]]

while t < t_max:
    h = h0  # Initial step size

    # Attempt a step using RKF45
    t_new, y_new, x_new = runge_kutta_fehlberg(pendulum_system, t, y, h, g, L)

    # Calculate the estimated local error
    error = np.linalg.norm(y_new - x_new)

    # Adapt the step size based on the error
    if error < 1e-6:
        t = t_new
        y = y_new
        x = x_new
        t_values.append(t)
        theta_values.append(y[0])
        omega_values.append(y[1])

    #h0 = h*min(max(0.9 * (1e-6 / error) ** 0.2, 0.3), 2.0)
    hnew = 0.9*h*(np.abs(h)*error/(x*(t0+h)-y*(t0+h)))**0.25

# Convert lists to NumPy arrays
t_values = np.array(t_values)
theta_values = np.array(theta_values)

# Plot the results
plt.figure(figsize=(10, 6))
#plt.plot(t_values, theta_values, label='Pendulum Angle (θ)')
plt.plot(theta_values, omega_values, label='Pendulum Angular Velocity (ω)')
plt.xlabel('Time (s)')
plt.ylabel('Angle (radians)')
plt.title('Nonlinear Pendulum Simulation using RKF45')
plt.legend()
plt.grid(True)
plt.show()

