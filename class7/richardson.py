from mpmath import mp, fac, harmonic
import matplotlib.pyplot as plt

mp.dps = 30  # Set the desired precision (adjust as needed)

def partial(nmax, s):
    return mp.nsum(lambda n: mp.power(n, -s), [1, nmax])

def Richardson(p, s):
    result = mp.mpf(0)
    for k in range(p + 1):
        term = ((-1)**(k + p) * partial(k + p, s) * mp.power(k + p, p) / (fac(k) * fac(p - k)))
        result += term
    return result

# Example usage:
mp.dps = 100  # Set precision for the example
p = 50  # Replace with your desired value of p
s = 3/2  # Replace with your desired value of s
result = []
for i in range(20):
    p+=1
    result.append(Richardson(p, s))

# plot result in log scale scatter
plt.scatter(range(20), result)
plt.yscale('log')
plt.show()
