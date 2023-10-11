import random
import numpy as np
import matplotlib.pyplot as plt
import sys
import Dmatrix


# Store the station coordinates for plotting
 
station_coords = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (9,8), (10,2)]
N = len(station_coords)
D = Dmatrix.generate_distance_matrix(station_coords)
# Define the number of stations (N) and the distance matrix D

initial_temperature = 1000
cooling_rate = 0.99

# Initialize the best tour and length
best_tour = []
best_length = sys.maxsize  

current_temperature = initial_temperature

# Create lists to store best tours and their lengths for each iteration
best_tours_history = []
best_lengths_history = []

# Step 0: choose an arbitrary starting permutation {s_i}_1^N
starting_permutation = list(range(1, N + 1))
random.shuffle(starting_permutation)

# Step 1: Initialize the current tour (c) with the starting permutation
current_tour = starting_permutation

while current_temperature > 1e-6:  # Adjust the threshold as needed
    # Calculate the length (d) of the current tour
    total_length = sum(D[current_tour[i] - 1][current_tour[i + 1] - 1] for i in range(N - 1))
    total_length += D[current_tour[N - 1] - 1][current_tour[0] - 1]

    i = 1

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

    # Check if the current solution is the best found so far
    if total_length < best_length:
        best_tour = current_tour.copy()
        best_length = total_length

    # Append the current best tour and length to the history lists
    best_tours_history.append(best_tour)
    best_lengths_history.append(best_length)
    
    # Reduce the temperature using the cooling rate
    current_temperature *= cooling_rate

# Plot the last best tour
plt.figure(figsize=(10, 6))
plt.scatter([coord[0] for coord in station_coords], [coord[1] for coord in station_coords],
            c='blue', marker='o', label='Stations', s=100)

# Add labels for each point
for i, coord in enumerate(station_coords):
    plt.text(coord[0], coord[1], str(i + 1), fontsize=11, ha='center', va='center', color='white')

# Create lines to represent the last best tour
tour_x = [station_coords[i - 1][0] for i in best_tour]
tour_y = [station_coords[i - 1][1] for i in best_tour]
tour_x.append(station_coords[best_tour[0] - 1][0])
tour_y.append(station_coords[best_tour[0] - 1][1])

# Print the final best tour and length
print("Best Tour:", best_tour)
print("Best Length:", best_length)

# Plot the last best tour
plt.plot(tour_x, tour_y, c='red', linestyle='-', marker='o', label='Best Tour', markersize=8)
plt.title("Last Best TSP Solution")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend()
plt.grid(True)
plt.show()
