import random
import math

def generate_random_D_and_points(N, max_coordinate=100):
    # Generate N random points with positive coordinates within the specified range
    points = [(random.uniform(0, max_coordinate), random.uniform(0, max_coordinate)) for _ in range(N)]

    # Calculate the distance matrix based on the Euclidean distance between the points
    distance_matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i != j:
                distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
                distance_matrix[i][j] = distance

    return distance_matrix, points

# Example usage:
N = 10  # Number of points
max_coordinate = 100  # Maximum coordinate for random points

distance_matrix, random_points = generate_random_D_and_points(N, max_coordinate)

# Print the random points in the desired format
print("Random Points:")
for i, point in enumerate(random_points):
    print(f"({point[0]}, {point[1]}),")

print("\nDistance Matrix:")
# Print the distance matrix in the desired format
for row in distance_matrix:
    print("[", end=" ")
    for dist in row:
        print(f"{dist:.2f},", end=" ")
    print("],")

