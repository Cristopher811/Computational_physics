import math
from pickle import EMPTY_LIST

def prime(n):
    if n<=1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def matryoshka(number):
    if prime(number) and number > 10:
        num_str = str(number)
        num_digits = len(num_str)
        result = [int(num_str[0])]
        for i in range(1,num_digits):
            combined = int(num_str[0])
            for j in range(1,i+1):
                combined = combined*10+int(num_str[j])
            result.append(combined)
        matryo = []
        for k in result:
            if prime(k):
                matryo.append(number)
            else:
                return 0
        return matryo
    else:
        return 0


def filter(lst):
    new_lst = []
    for sub_lst in lst:
        if any(i==j for i,j in zip(sub_lst, sub_lst[1:])):
            new_lst.append(sub_lst[0])
    return new_lst

number=0
megalist = []
valid = True
while number<10**10:
    number+=1
    if matryoshka(number) == 0:
        valid = False
    else:
        megalist.append(matryoshka(number))
print(filter(megalist))
