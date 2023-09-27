import math

def generate_circle_points(center, radius, num_points):
    points = []

    # Calculate the angle increment between each point
    angle_increment = 2 * math.pi / num_points

    # Generate points in the upper half of the circle
    for i in range(num_points // 2):
        angle = i * angle_increment
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))

    # Mirror the upper half to create the lower half of the circle
    for x, y in points[:0:-1]:
        points.append((x, 2 * center[1] - y))

    return points

center = (30, 40)  # Center of the circle
radius = 10.0  # Radius of the circle
num_points = 120  # Number of points to generate

circle_points = []
circle_points.append(generate_circle_points(center, radius, num_points))

# Print the generated points
print(circle_points)
