import math
import time

def prime(n):
    eta=1
    for i in range(n-2):
        ratio=float(n)/float(i+2)
        fratio=math.floor(ratio)
        if ratio-fratio==0.0:
            eta=0
            break
    return eta

def bestprime(n):
    eta=1
    for i in range(int(n/2)):
        mod=float(n%(i+2))
        if mod==0.0:
            eta=0
    return eta

def findprimes(n):
    primes = []
    for i in range(2,n+1):
        if prime(i):
            primes.append(i)
    return primes

def primorial(n):
    primes = findprimes(n)
    primorial=1
    for i in primes:
        primorial *= i
    return primorial

#n = int(input('Enter a number: '))
#print(bestprime(n))
#primes = findprimes(n)
#print(primes)
#print(primorial(n))
#print(prime(primorial(n)+1))

print(findprimes(999))












start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
