import random
import matplotlib.pyplot as plt
import sys

# Define the number of stations (N) and the distance matrix D
N = 10  # You can change this to the number of stations you have
D = [[ 0.00, 23.08, 70.57, 86.45, 85.18, 59.11, 34.76, 25.12, 70.32, 57.22, ],
[ 23.08, 0.00, 55.66, 73.09, 71.52, 36.95, 42.29, 3.33, 57.80, 43.30, ],
[ 70.57, 55.66, 0.00, 17.83, 16.10, 34.77, 54.82, 57.08, 8.18, 13.38, ],
[ 86.45, 73.09, 17.83, 0.00, 1.90, 51.34, 65.79, 74.66, 16.16, 29.90, ],
[ 85.18, 71.52, 16.10, 1.90, 0.00, 49.45, 65.14, 73.05, 15.03, 28.42, ],
[ 59.11, 36.95, 34.77, 51.34, 49.45, 0.00, 62.59, 36.29, 41.49, 30.42, ],
[ 34.76, 42.29, 54.82, 65.79, 65.14, 62.59, 0.00, 45.62, 50.71, 43.11, ],
[ 25.12, 3.33, 57.08, 74.66, 73.05, 36.29, 45.62, 0.00, 59.61, 45.04, ],
[ 70.32, 57.80, 8.18, 16.16, 15.03, 41.49, 50.71, 59.61, 0.00, 14.60, ],
[ 57.22, 43.30, 13.38, 29.90, 28.42, 30.42, 43.11, 45.04, 14.60, 0.00, ]]
#[
#    [0, 2, 4, 1, 3],
#    [2, 0, 3, 2, 4],
#    [4, 3, 0, 3, 1],
#    [1, 2, 3, 0, 2],
#    [3, 4, 1, 2, 0]
#]

# Set the initial temperature and cooling rate
initial_temperature = 1000.0
cooling_rate = 0.99
max_iterations = 10000

# Initialize the best tour and length
best_tour = []
best_length = sys.maxsize  

# Store the station coordinates for plotting
station_coords = [(40.03614738787713, 99.13126603933098),
(26.090188662520852, 80.74216691968556),
(46.17005457410017, 28.82844423600033),
(56.440840107194155, 14.25300584861484),
(54.81470158749266, 15.24209664218339),
(15.563011352347944, 45.32030218532643),
(68.34160803276237, 78.96020792554769),
(22.761025111210675, 80.8889845975676),
(54.2263801327674, 30.25764446906819),
(45.82201574929886, 42.20202517871551)]

current_temperature = initial_temperature

while current_temperature > 1e-3:  # Adjust the threshold as needed
    # Choose an arbitrary starting permutation {s_i}_1^N
    starting_permutation = list(range(1, N + 1))
    random.shuffle(starting_permutation)

    # Initialize the current tour (c) with the starting permutation
    current_tour = starting_permutation

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

    # Reduce the temperature using the cooling rate
    current_temperature *= cooling_rate

# Print the best tour and length
print("Best Tour:", best_tour)
print("Best Length:", best_length)

# Plot the station points
plt.scatter([coord[0] for coord in station_coords], [coord[1] for coord in station_coords],
            c='blue', marker='o', label='Stations', s=100)

# Add labels for each point
for i, coord in enumerate(station_coords):
    plt.text(coord[0], coord[1], str(i + 1), fontsize=11, ha='center', va='center', color='white')

# Create lines to represent the best tour
tour_x = [station_coords[i - 1][0] for i in best_tour]
tour_y = [station_coords[i - 1][1] for i in best_tour]
tour_x.append(station_coords[best_tour[0] - 1][0])
tour_y.append(station_coords[best_tour[0] - 1][1])

# Plot the best tour
plt.plot(tour_x, tour_y, c='red', linestyle='-', marker='o', label='Best Tour', markersize=8)

plt.title("TSP Solution")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
