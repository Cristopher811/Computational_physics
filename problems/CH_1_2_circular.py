import math
from pickle import EMPTY_LIST

def prime(n):
    if n<=1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def circular_prime(p):
    if prime(p) and p > 10:
        p_str = str(p)
        permutations = []
        for i in range(len(p_str)):
            circular_p = int(p_str[i:] + p_str[:i])
            permutations.append(circular_p)
        prime_permutations = []
        for k in permutations:
            if prime(k):
                prime_permutations.append(p)
        return prime_permutations
    else:
        return EMPTY_LIST


def filter(lst):
    new_lst = []
    for sub_lst in lst:
        valid = True
        for num in sub_lst:
            if len(sub_lst) != len(str(num)) or sub_lst == EMPTY_LIST:
                valid = False
                break
        if valid and any(i==j for i,j in zip(sub_lst, sub_lst[1:])):
            new_lst.append(sub_lst[0])
    return new_lst

megalist = []
number=0
while number<10**6:
    number+=1
    megalist.append(circular_prime(number))
result = filter(megalist)
print(result,len(result))

#There are 51 circular primes in the first 10**6 positive entire numbers
