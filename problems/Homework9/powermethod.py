import numpy as np
import matplotlib.pyplot as plt

# Enable LaTeX rendering in matplotlib plots
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    })

# Generate a random n x n orthogonal matrix

nn=500
random_matrix = np.random.rand(nn,nn)
# Add the transpose of the matrix to ensure it is symmetric 
mat = random_matrix + random_matrix.T

def power_method(mat,niter):
    nn = len(mat)
    result = []
    vec = np.random.rand(nn) # generate a random vector to start with
    norm = np.linalg.norm(vec) # calculate the norm of the vector
    nvec = vec/norm # normalize the vector
    vec2 = np.dot(mat,vec) # calculate the dot product of the matrix and the vector
    expectation = np.dot(nvec,vec2) # calculate the expectation value
    sigma = np.sqrt(np.dot(vec2,vec2)-expectation**2) # calculate the variance
    result.append([expectation,sigma])
    for i in range(niter):
        vec1 = np.dot(mat,nvec)
        norm1 = np.linalg.norm(vec1)
        nvec1 = vec1/norm1
        vec2 = np.dot(mat,vec1)
        expectation = np.dot(nvec1,vec2)
        sigma = np.sqrt(np.dot(vec2,vec2)-expectation**2)
        result.append([expectation,sigma])
        nvec = nvec1

    # Lists the store average and sigma values
    average_values = [res[0] for res in result]
    sigma_values = [res[1] for res in result]
    return nvec,average_values,sigma_values

niter = 20
result = power_method(mat,niter)
nvec = result[0]
average_values = result[1]
sigma_values = result[2]


print(nvec)
# Plot the results
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(average_values,marker='o',linestyle='-',color='blue')
plt.xlabel("iteration")
plt.ylabel("average")
plt.subplot(1,2,2)
plt.plot(sigma_values,marker='o',linestyle='-',color='red')
plt.yscale('log')
plt.xlabel("iteration")
plt.ylabel("sigma")
plt.show()
