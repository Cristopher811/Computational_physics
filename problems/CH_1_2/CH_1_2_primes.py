import time

def bestprime(n):
    if n<=1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def findprimes(n):
    primes = []
    for i in range(2,n+1):
        if bestprime(i):
            primes.append(i)
    return primes

def primorial(n):
    if bestprime(n):
        primes = findprimes(n)
        primorial=1
        for i in primes:
            primorial *= i
        if bestprime(primorial + 1) or bestprime(primorial - 1):
            return n
        else:
            return 0
    else:
        return 0


# ----------------------------------------------------------------------------------------------------- #

# To see the bestprime() function work uncomment this line:

#print(bestprime(31))

# ----------------------------------------------------------------------------------------------------- #

# To see the findprimes() function work uncomment this line:

#print(findprimes(n))

# ----------------------------------------------------------------------------------------------------- #

# To see the primorial() function work uncomment this line:

#print(primorial(5))

# ----------------------------------------------------------------------------------------------------- #


# To get the primorials under the first 50 natural numbers uncomment the following lines:

#primorials = []
#n = 1
#while n<50:
#    n+=1
#    if primorial(n) != 0:
#        primorials.append(primorial(n))
#
#print(primorials)












start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
