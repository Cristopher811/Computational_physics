from pickle import EMPTY_LIST
import math



def prime(n):
    if n<=1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_permutations(num):
    if prime(num) and num>10:
        def permute(n,l,r):
            if l==r:
                permutations.append(int(''.join(n)))
            else:
                for i in range(l,r+1):
                    n[l], n[i] = n[i], n[l]
                    permute(n,l+1,r)
                    n[l], n[i] = n[i], n[l]

        permutations = []
        n = list(str(number))
#        print(n)
        permute(n,0,len(n)-1)
        return permutations
#        primepermutations = []
#        for k in permutations:
#            if prime(k):
#                primepermutations.append(number)
#        return primepermutations
    else:
        return EMPTY_LIST

def filter(lst):
    new_lst = []
    for sub_lst in lst:
        valid = True
        for num in sub_lst:
            if len(sub_lst) != math.factorial(len(str(num))) or sub_lst == EMPTY_LIST:
                valid = False
                break
        if valid and any(i==j for i,j in zip(sub_lst, sub_lst[1:])):
            new_lst.append(sub_lst[0])
    return new_lst

megalist = []
number = 558541
print(get_permutations(number))
print(len(get_permutations(number)))
#while number<10**5:
#    number+=1
#    megalist.append(get_permutations(number))
#print(filter(megalist))



#permus = []
#while number<10**6:
#    number+=1
