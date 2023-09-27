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
N = 50  # Number of points
max_coordinate = 100  # Maximum coordinate for random points

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def generate_distance_matrix(positions):
    num_points = len(positions)
    distance_matrix = [[0.0 for _ in range(num_points)] for _ in range(num_points)]

    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                distance = euclidean_distance(positions[i], positions[j])
                distance_matrix[i][j] = distance

    return distance_matrix



# Print the random points in the desired format
print(generate_random_D_and_points(N,max_coordinate)[1])
#for i, point in enumerate(random_points):
#    print(f"({point[0]}, {point[1]}),")
#
#print("\nDistance Matrix:")
## Print the distance matrix in the desired format
#for row in distance_matrix:
#    print("[", end=" ")
#    for dist in row:
#        print(f"{dist:.2f},", end=" ")
#    print("],")
#
