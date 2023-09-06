import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

filename = "output2.txt" 

# Step 1: Open the .txt file
with open(filename, "r") as file:
    # Step 2: Read all the lines from the file
    lines = file.readlines()

    # Step 3: Create an empty list
    values = []

    # Step 4 and 5: Iterate through the lines and convert to float, append to the list
    for line in lines:
        value = float(line.strip())  # Convert to float
        values.append(value)  # Append to the list

print(len(values))
range_min = min(values)
range_max = max(values)
num_bins = len(set(values))

plt.hist(values, bins=num_bins, range=(range_min, range_max), density=True)


mu, std = norm.fit(values)
x = np.linspace(range_min, range_max, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'r')

plt.axvline(x=44.0, color='red', linestyle='--')

plt.legend(['Gaussian Fit'])
plt.show()

