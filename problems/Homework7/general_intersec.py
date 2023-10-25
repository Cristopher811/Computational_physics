import numpy as np
import matplotlib.pyplot as plt
from numba import jit

L = 0.5 # separation distance
d = 3 # dimension of the problem
num_samples = 10**4
trials = 10**3

@jit(nopython=True)
def generate_points(L,d):
    x_limit = 1 - L/2
    yzw_limit = np.sqrt(1-(L/2)**2)
    point = np.zeros(d)
    for i in range(1,d):
        point[0] = np.random.uniform(-x_limit,x_limit)
        point[i] = np.random.uniform(-yzw_limit,yzw_limit)
    return point
@jit(nopython=True)
def sum_after0(point,d):
    sum_after0 = 0
    for i in range(1,d):
        sum_after0 += point[i]**2
    return sum_after0

@jit(nopython=True)
def montecarlo_method(L,d,num_samples):
    x_limit = 1 - L/2
    yzw_limit = np.sqrt(1-(L/2)**2)
    count = 0
    
    volumeyzw = 1
    for _ in range(1,d):
        volumeyzw *= abs(yzw_limit)
    exact = 2**d*(volumeyzw*abs(x_limit))
    sum_after = 0
    for _ in range(num_samples):
        point = generate_points(L,d)
        sum_after = sum_after0(point,d)
        if np.sqrt((point[0]+L/2)**2 + sum_after) < 1 and np.sqrt((point[0]-L/2)**2 + sum_after) < 1:
            count += 1
    return exact*count/num_samples

@jit(nopython=True)
def run_trials(L,d,num_samples,trials):
    mc_values = np.zeros(trials)
    for i in range(trials):
        mc_values[i] = montecarlo_method(L,d,num_samples)
    return mc_values

approx = montecarlo_method(L,d,num_samples)
print(approx)

result = run_trials(L,d,num_samples,trials)
average = np.mean(result)
print(average)
plt.show()
