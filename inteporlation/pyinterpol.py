import numpy as np
import matplotlib.pyplot as plt

# Define the original function
def f(x):
    return 1 / (1 + 100 * x**2)

# Define the Lagrange interpolation functions
def P(j, n, x, points):
    result = 1
    for k in range(n):
        if k != j:
            result *= (x - points[k]) / (points[j] - points[k])
    return result

def lagrange_interpolation(n, x, points, values):
    result = 0
    for j in range(n):
        result += values[j] * P(j, n, x, points)
    return result

# Define the range of x values
x_values = np.linspace(-1, 1, 400)

# Define the interpolation points
points = np.linspace(-1, 1, 11)
values = f(points)

# Compute the interpolated values
interpolated_values = [lagrange_interpolation(len(points), x, points, values) for x in x_values]

# Create a plot of the original function
plt.plot(x_values, [f(x) for x in x_values], label="Original Function", color="blue")

# Create a plot of the Lagrange interpolation
plt.plot(x_values, interpolated_values, "ro-", label="Lagrange Interpolation", markersize=4)

# Set axis labels and legend
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Show the plot
plt.title("Original Function vs. Lagrange Interpolation")
plt.grid()
plt.show()


