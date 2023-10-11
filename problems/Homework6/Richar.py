import mpmath as mp

mp.dps = 100
k = 100
s = 3/2

def partial(nmax, s):
    return mp.nsum(lambda n: mp.power(n, -s), [1, nmax])

A = mp.matrix([0,0,0,0])

for i in range(len(A)):
    # add the value of the partial function to the matrix A
    nmax = i+k
    A[i] = partial(nmax, s)

M = mp.matrix([[1,1/k**(s-1),1/k**s,1/k**(s+1)],[1,1/(k+1)**(s-1),1/(k+1)**s,1/(k+1)**(s+1)],[1,1/(k+2)**(s-1),1/(k+2)**s,1/(k+2)**(s+1)],[1,1/(k+3)**(s-1),1/(k+3)**s,1/(k+3)**(s+1)]])
Minv = mp.inverse(M)

Q = Minv*A
print(Q)
#
#
#B = mp.matrix([0,0,0,0,0])
#for i in range(len(B)):
#    nmax = i+k
#    B[i] = partial(nmax, s)
#
#T = mp.matrix([[1, 1/k**(s - 1), 1/k**(s), 1/k**(s + 1),1/k**(s + 3)],[1, 1/(k + 1)**(s - 1), 1/(k + 1)**(s), 1/(k + 1)**(s + 1), 1/(k + 1)**(s + 3)],[1, 1/(k + 2)**(s - 1), 1/(k + 2)**(s), 1/(k + 2)**(s + 1),1/(k + 2)**(s + 3)], [1, 1/(k + 3)**(s - 1), 1/(k + 3)**(s), 1/(k + 3)**(s + 1), 1/(k + 3)**(s + 3)],[1,1/(k + 4)**(s - 1), 1/(k + 4)**(s), 1/(k + 4)**(s + 1), 1/(k + 4)**(s + 3)]])
#Tinv = mp.inverse(T)
#
#Q2 = Tinv*B
#print(Q2)

z = mp.zeta(3/2)
print(z)
