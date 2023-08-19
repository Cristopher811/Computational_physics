import time
def Q(n,d):
    n = str(n)
#    if '.' in n:
#      n = n.replace('.','')
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

n = float(input('Enter a number: '))
d = int(input('Enter the digit: '))
print(Q(n,d))

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
