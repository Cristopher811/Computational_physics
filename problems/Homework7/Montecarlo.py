import numpy as np
import random
import time
import matplotlib.pyplot as plt
from numba import jit

# Constants
d = 2
nmax = 5000
trials = 10000
exact_area = 6*np.pi/7

@jit(nopython=True)
def generate_point(d):
    x = np.random.uniform(-1,1,d)
    return x, np.sum(x**2)

@jit(nopython=True)
def mc_trial(d,nmax):
    count = 0
    for _ in range(nmax):
        point, sum_of_squares = generate_point(d)
        if abs(point[1])<1/7*np.sin(2*np.arccos(point[0]))+6/7*np.sqrt(1-point[0]**2):
            count += 1
    return (2**d)*count/nmax

def run_trials(d,nmax,trials):
    mc_values = np.zeros(trials)
    for i in range(trials):
        mc_values[i] = mc_trial(d,nmax)
    return mc_values

def gaussian(x,average,stdev,trials):
    return np.exp(-(x-average)**2/2/stdev**2)/np.sqrt(2*np.pi*stdev**2)

def main():
    start_time = time.time()
    result = mc_trial(d,nmax)
    end_time = time.time()

    print("n =",nmax)
    print("Approximate area:",result)
    print("Exact area=",exact_area)
    print("% error:",100*(1-result/exact_area))
    print("Time for a single mc:",end_time-start_time)
    start_time = time.time()
    mc_values = run_trials(d,nmax,trials)
    end_time = time.time()
    print("Time for all trials:",end_time-start_time)
    with open('data_hit.dat','wb') as f:
        np.savetxt(f,mc_values)
    average = np.mean(mc_values)
    stdev = np.std(mc_values)
    print("Average:",average)
    print("Exact area = ",exact_area)
    print("Standard deviation:",stdev)
    print("Left = ",average-stdev)
    print("Right = ",average+stdev)

# Read data from file
    with open('data_hit.dat','r') as file:
        data = [float(line.strip()) for line in file]

# Create a histogram
        plt.hist(data, bins=60, density=True, alpha=0.6, color='b',edgecolor='k')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram of Data')
        plt.grid(True)
        plt.show()


        ymax = 17.5
        x = np.array([average - stdev, average - stdev])
        y = np.array([0, ymax])
        plt.plot(x,y,color='k',linestyle='dashed',linewidth=1)
        x = np.array([average + stdev, average + stdev])
        y = np.array([0, ymax])
        plt.plot(x,y,color='k',linestyle='dashed',linewidth=1)
        x = np.array([average, average])
        y = np.array([0, ymax])
        plt.plot(x,y,color='k',linestyle='solid',linewidth=1)
        x = np.arange(average-3*stdev,average+3*stdev,0.001)
        y = gaussian(x,average,stdev,trials)
        plt.plot(x,y,'r')
        exact = exact_area
        x = np.array([exact, exact])
        y = np.array([0, ymax])
        plt.plot(x,y,color='r',linestyle='dashed',linewidth=1)

        plt.savefig('Fig_Hit_or_miss.eps',format='eps',dpi=300,bbox_inches='tight')

        plt.show()

if __name__ == "__main__":
    main()
