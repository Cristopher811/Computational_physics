from mpmath import mp, fac, harmonic

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
p = 24  # Replace with your desired value of p
s = 2  # Replace with your desired value of s
result = Richardson(p, s)
print(result)
