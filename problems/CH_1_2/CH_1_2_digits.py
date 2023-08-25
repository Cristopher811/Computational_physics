import time

def Q(n,d):
    n = str(n)
    digits = list(n)

    if '.' in digits:
        index = digits.index('.')
        del digits[index+1:]
        digits.pop(index)
        digits = [int(i) for i in digits]
        return digits[(d-len(digits))*(-1)]
    else:
        digits = [int(i) for i in digits]
        return digits[(d-len(digits))*(-1)]

def lstdigits(n):
    n = str(n)
    if '.' in n:
      n = n.replace('.','')
    digits = list(n)
    digits = [int(i) for i in digits]
    return digits

# To check the Q(n,d) function only uncomment the following lines and erase the previous:

#n = float(input('Enter a number: '))
#d = int(input('Enter the digit: '))
#print(Q(n,d))

# -------------------------------------------------------------------------------------------------- #

# To create an list of lists where each sublist contains the digits of the first 200 natural numbers
# uncomment the next lines: 

#n = 0
#digits_list = []
#while n<200:
#    n+=1
#    digits_list.append(lstdigits(n))
#print(digits_list)

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
