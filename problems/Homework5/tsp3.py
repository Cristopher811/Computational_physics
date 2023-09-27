import random
import numpy as np
import matplotlib.pyplot as plt
import sys
import Dmatrix


# Store the station coordinates for plotting
 
station_coords = [(40.0, 40.0), (39.986295347545735, 40.52335956242944), (39.94521895368273, 41.045284632676534), (39.876883405951375, 41.56434465040231), (39.78147600733806, 42.079116908177596), (39.65925826289068, 42.588190451025206), (39.510565162951536, 43.09016994374947), (39.33580426497202, 43.583679495453005), (39.13545457642601, 44.067366430758), (38.91006524188368, 44.53990499739547), (38.66025403784439, 45.0), (38.38670567945424, 45.44639035015027), (38.09016994374947, 45.877852522924734), (37.77145961456971, 46.29320391049838), (37.43144825477394, 46.691306063588584), (37.071067811865476, 47.071067811865476), (36.691306063588584, 47.43144825477394), (36.29320391049838, 47.77145961456971), (35.877852522924734, 48.09016994374947), (35.446390350150274, 48.38670567945424), (35.0, 48.66025403784438), (34.53990499739547, 48.91006524188368), (34.067366430758, 49.13545457642601), (33.583679495453005, 49.33580426497202), (33.09016994374947, 49.510565162951536), (32.58819045102521, 49.65925826289068), (32.079116908177596, 49.78147600733806), (31.564344650402308, 49.876883405951375), (31.045284632676537, 49.94521895368273), (30.52335956242944, 49.986295347545735), (30.0, 50.0), (29.476640437570563, 49.986295347545735), (28.954715367323466, 49.94521895368273), (28.435655349597692, 49.876883405951375), (27.920883091822407, 49.78147600733806), (27.411809548974794, 49.65925826289068), (26.909830056250527, 49.510565162951536), (26.416320504547, 49.33580426497202), (25.932633569242, 49.135454576426014), (25.460095002604533, 48.91006524188368), (25.0, 48.66025403784439), (24.553609649849733, 48.386705679454245), (24.12214747707527, 48.09016994374947), (23.706796089501626, 47.77145961456971), (23.308693936411423, 47.43144825477395), (22.928932188134524, 47.071067811865476), (22.56855174522606, 46.691306063588584), (22.228540385430293, 46.29320391049838), (21.909830056250527, 45.877852522924734), (21.613294320545762, 45.446390350150274), (21.339745962155614, 45.0), (21.08993475811632, 44.53990499739547), (20.864545423573993, 44.06736643075801), (20.664195735027985, 43.583679495453005), (20.489434837048464, 43.09016994374947), (20.34074173710932, 42.58819045102521), (20.218523992661943, 42.079116908177596), (20.123116594048625, 41.56434465040231), (20.054781046317267, 41.045284632676534), (20.013704652454262, 40.52335956242944), (20.013704652454262, 39.47664043757056), (20.054781046317267, 38.954715367323466), (20.123116594048625, 38.43565534959769), (20.218523992661943, 37.920883091822404), (20.34074173710932, 37.41180954897479), (20.489434837048464, 36.90983005625053), (20.664195735027985, 36.416320504546995), (20.864545423573993, 35.93263356924199), (21.08993475811632, 35.46009500260453), (21.339745962155614, 35.0), (21.613294320545762, 34.553609649849726), (21.909830056250527, 34.122147477075266), (22.228540385430293, 33.70679608950162), (22.56855174522606, 33.308693936411416), (22.928932188134524, 32.928932188134524), (23.308693936411423, 32.56855174522605), (23.706796089501626, 32.22854038543029), (24.12214747707527, 31.909830056250527), (24.553609649849733, 31.613294320545755), (25.0, 31.33974596215561), (25.460095002604533, 31.08993475811632), (25.932633569242, 30.864545423573986), (26.416320504547, 30.66419573502798), (26.909830056250527, 30.489434837048464), (27.411809548974794, 30.34074173710932), (27.920883091822407, 30.218523992661943), (28.435655349597692, 30.123116594048625), (28.954715367323466, 30.054781046317267), (29.476640437570563, 30.013704652454265), (30.0, 30.0), (30.52335956242944, 30.013704652454265), (31.045284632676537, 30.054781046317267), (31.564344650402308, 30.123116594048625), (32.079116908177596, 30.218523992661943), (32.58819045102521, 30.34074173710932), (33.09016994374947, 30.489434837048464), (33.583679495453005, 30.66419573502798), (34.067366430758, 30.864545423573993), (34.53990499739547, 31.08993475811632), (35.0, 31.339745962155618), (35.446390350150274, 31.613294320545762), (35.877852522924734, 31.909830056250527), (36.29320391049838, 32.22854038543029), (36.691306063588584, 32.56855174522606), (37.071067811865476, 32.928932188134524), (37.43144825477394, 33.308693936411416), (37.77145961456971, 33.70679608950162), (38.09016994374947, 34.122147477075266), (38.38670567945424, 34.55360964984973), (38.66025403784439, 35.0), (38.91006524188368, 35.46009500260453), (39.13545457642601, 35.932633569242), (39.33580426497202, 36.416320504546995), (39.510565162951536, 36.90983005625053), (39.65925826289068, 37.411809548974794), (39.78147600733806, 37.920883091822404), (39.876883405951375, 38.43565534959769), (39.94521895368273, 38.954715367323466), (39.986295347545735, 39.47664043757056)]
N = len(station_coords)
print(N)
D = Dmatrix.generate_distance_matrix(station_coords)
# Define the number of stations (N) and the distance matrix D

initial_temperature = 1000
cooling_rate = 0.999

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

while current_temperature > 1e-3:  # Adjust the threshold as needed

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

# Create a line plot to visualize the convergence of lengths
plt.plot(best_lengths_history, marker='o', linestyle='-', color='b')
plt.title("Convergence of Lengths")
plt.xlabel("Iteration")
plt.ylabel("Length")
plt.grid(True)
plt.show()


