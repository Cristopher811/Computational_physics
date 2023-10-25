import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt

def is_inside(x, r):
    return np.sum(x**2) <= r**2

def intersection_points(L, d, num_samples, exact):
    if L >= 2:
        return 0

    intersection_x1 = []
    intersection_x2 = []

    for _ in range(num_samples):
         # Sample points in all quadrants by using random numbers in [-1, 1]
        x1 = (2 * np.random.rand(d) - 1) * np.array([1, -1])
        x2 = (2 * np.random.rand(d) - 1) * np.array([1, -1])

        x2[0] += L

        if is_inside(x1, 1) and is_inside(x2, 1):
            intersection_x1.append(x1)
            intersection_x2.append(x2)

    if d == 2:
        if L == 0:
            # When L is 0, the intersection is a single unit circle
            estimated_area = (len(intersection_x1) / num_samples) *np.pi*1.63
        else:
            estimated_area = (len(intersection_x1) / num_samples) * 4
    else:
        estimated_area = (len(intersection_x1) / num_samples) * exact*4

    return estimated_area, intersection_x1, intersection_x2

def plot_circles_and_intersections(L, intersection_x1, intersection_x2):
    fig, ax = plt.subplots()
    
    # Plot the first circle
    circle1 = plt.Circle((0, 0), 1, fill=False, color='r', linestyle='dotted', linewidth=2)
    ax.add_patch(circle1)

    if L > 0:
        # Plot the second circle only if L is not 0
        circle2 = plt.Circle((L, 0), 1, fill=False, color='g', linestyle='dotted', linewidth=2)
        ax.add_patch(circle2)

    # Plot the intersection points
    intersection_x1 = np.array(intersection_x1)
    intersection_x2 = np.array(intersection_x2)
    plt.scatter(intersection_x1[:, 0], intersection_x1[:, 1], c='b', label='Intersection Points 1')
    plt.scatter(intersection_x2[:, 0], intersection_x2[:, 1], c='y', label='Intersection Points 2')

    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlim(-1.5, L+1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Circles and Intersection Points')
    ax.legend()
    plt.grid(True)
    plt.show()

def main():
    L = 1
    num_trials = 10**4
    d = 2
    num_samples = 10**4

    exact = np.pi**(d/2) / gamma(d/2 + 1)

    result, intersection_x1, intersection_x2 = intersection_points(L, d, num_samples, exact)

    print("Number of samples:", num_samples)
    print("Approximate volume/area of intersection:", result)

    plot_circles_and_intersections(L, intersection_x1, intersection_x2)

if __name__ == '__main__':
    main()

