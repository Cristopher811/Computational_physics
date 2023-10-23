import numpy as np
from scipy.special import gamma
from numba import jit
import matplotlib.pyplot as plt

@jit(nopython=True)
def is_inside(x, r):
    return np.sum(x**2) <= r**2

@jit(nopython=True)
def montecarlo(L, d, num_samples, exact):
    if L >= 2:
        return 0

    intersection_points = 0

    for _ in range(num_samples):
        x1 = 2 * np.random.rand(d) - 1
        x2 = 2 * np.random.rand(d) - 1

        x2[0] += L

        if is_inside(x1, 1) and is_inside(x2, 1):
            intersection_points += 1

    if d == 2:
        estimated_area = (intersection_points / num_samples) * 4
    else:
        estimated_area = (intersection_points / num_samples) * 4 * exact

    return estimated_area

@jit(nopython=True)
def simulate_trials(L, num_trials, d, num_samples, exact):
    intersection_volumes = np.zeros(num_trials)
    for i in range(num_trials):
        intersection_volumes[i] = montecarlo(L, d, num_samples, exact)
    return intersection_volumes



def main():
    L = 1
    num_trials = 10**4
    d = 2
    num_samples = 10**4

    exact = np.pi**(d/2) / gamma(d/2 + 1)

    result = montecarlo(L, d, num_samples, exact)

    print("Number of samples:", num_samples)
    print("Approximate volume/area of intersection:",result)

    intersection_volumes = simulate_trials(L, num_trials, d, num_samples, exact)

    with open('data.dat', 'wb') as f:
        np.savetxt(f, intersection_volumes)

    average = np.mean(intersection_volumes)
    stdev = np.std(intersection_volumes)
    print("Average intersection volume:", average)
    print("Standard deviation:", stdev)

    with open('data.dat','r') as file:
        data = [float(line.strip()) for line in file]

        plt.hist(data,bins=60, density=True, alpha=0.6, color='b',edgecolor='k')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Intersection Volume Histogram')
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    main()
