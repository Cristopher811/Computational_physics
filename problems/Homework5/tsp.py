import random
import matplotlib.pyplot as plt

# Define the number of stations (N) and the distance matrix D
N = 5  # You can change this to the number of stations you have
D = [
    [0, 2, 4, 1, 3],
    [2, 0, 3, 2, 4],
    [4, 3, 0, 3, 1],
    [1, 2, 3, 0, 2],
    [3, 4, 1, 2, 0]
    ]

# Set the initial temperature and maximum iterations
initial_temperature = 0.1
max_iterations = 10000

# Step 0: Choose an arbitrary starting permutation {s_i}_1^N
starting_permutation = list(range(1, N + 1))
random.shuffle(starting_permutation)

# Initialize the current tour (c) with the starting permutation
current_tour = starting_permutation

# Calculate the length (d) of the current tour
total_length = sum(D[current_tour[i] - 1][current_tour[i + 1] - 1] for i in range(N - 1))
total_length += D[current_tour[N - 1] - 1][current_tour[0] - 1]

i = 1

# Store the station coordinates for plotting
station_coords = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

while i <= N:
    # Step 3: Generate a random integer j, 1 <= j <= N, j ≠ i
    j = random.choice([x for x in range(1, N + 1) if x != i])

    # Step 4: Construct a trial permutation (t) based on i and j
    i_prime = min(i, j)
    j_prime = max(i, j)

    trial_tour = [0] * N

    for k in range(i_prime - 1):
        trial_tour[k] = current_tour[k]

    for k in range(j_prime - i_prime + 1):
        trial_tour[i_prime + k - 1] = current_tour[j_prime - k - 1]

    for k in range(j_prime, N):
        trial_tour[k] = current_tour[k]

    # Step 5: Calculate the length (d') of the trial permutation
    total_length_trial = D[trial_tour[N - 1] - 1][trial_tour[0] - 1]
    for k in range(N - 1):
        total_length_trial += D[trial_tour[k] - 1][trial_tour[k + 1] - 1]

    # Step 6: Accept or reject the trial solution based on the change in length and temperature
    if total_length_trial < total_length:
        current_tour = trial_tour
        total_length = total_length_trial

    # Step 8: Increase i by one
    i += 1

# Print the final tour and length
print("Final Tour:", current_tour)
print("Final Length:", total_length)

# Plot the station points
plt.figure(figsize=(8, 6))
plt.scatter([coord[0] for coord in station_coords], [coord[1] for coord in station_coords],
            c='blue', marker='o', label='Stations', s=100)

# Create lines to represent the final tour
tour_x = [station_coords[i - 1][0] for i in current_tour]
tour_y = [station_coords[i - 1][1] for i in current_tour]
tour_x.append(station_coords[current_tour[0] - 1][0])
tour_y.append(station_coords[current_tour[0] - 1][1])

# Plot the final tour
plt.plot(tour_x, tour_y, c='red', linestyle='-', marker='o', label='Final Tour', markersize=8)

plt.title("TSP Solution")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

