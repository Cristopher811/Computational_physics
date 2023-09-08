from mpmath import mp
import matplotlib.pyplot as plt
import mynrmethod as nr
import numpy as np

# Set the decimal places to a high value
mp.dps = 1200

# Helper function to calculate the nth term for BBP series
def bbp_term(n):
    return mp.mpf(1)/(16**n) * (
        mp.mpf(4)/(8*n + 1) -
        mp.mpf(2)/(8*n + 4) -
        mp.mpf(1)/(8*n + 5) -
        mp.mpf(1)/(8*n + 6)
    )

# Calculate the value of pi using BBP series
def calculate_pi():
    pi = mp.mpf(0)
    for k in range(0, mp.dps):
        pi += bbp_term(k)
    return pi



# Calculate the successive approximations of pi using both methods
newton_pi_approximations = []
bbp_pi_approximations = []

for i in range(1, 100):
    newton_pi_approximations.append(nr.pi(22/7, i, 1e-1200))
    bbp_pi_approximations.append(calculate_pi())

# Compute the differences between the successive approximations
differences = []
for i in range(0, len(newton_pi_approximations)):
#    differences.append(mp.fabs(newton_pi_approximations[i]/bbp_pi_approximations[i]))
    differences.append(mp.fabs(bbp_pi_approximations[i]/newton_pi_approximations[i]))

# Calculate the rate of convergence
convergence_rate = [] 
for i in range(0, len(differences)):
    convergence_rate.append(mp.log(differences[i])/np.log(2))

#convergence_rate = mp.log(differences[:-1] / differences[1:]) / np.log(2)

# Plot the rate of convergence
plt.plot(range(1, 100), convergence_rate)
plt.xlabel('Number of iterations')
plt.ylabel('Rate of convergence')
plt.title('Rate of Convergence of Newton-Raphson Method')
plt.grid(True)
plt.show()
#for i in range(1, 100):
#    newton_pi_approximations.append(nr.pi(22/7,i,1e-1200))
#    bbp_pi_approximations.append(calculate_pi())
#
#
## Compute the differences between the successive approximations
#differences = []
#for i in range(0, len(newton_pi_approximations)):
#    differences.append(abs(newton_pi_approximations[i] - bbp_pi_approximations[i]))
#print(differences)
#
#
#convergence_rate = []
#for i in range(0, len(differences)):
#    convergence_rate.append(mp.log(differences[i:])/np.log(2))
#    print(convergence_rate)
##differences = mp.fabs(for i in range 1000: newton_pi_approximations[i] - bbp_pi_approximations[i])
#
## Calculate the rate of convergence
##for i in range(0, len(differences)):
##    convergence_rate = np.log(differences[i])/np.log(2)
#
#
##convergence_rate = mp.log(differences[:-1] / differences[1:]) / np.log(2)
#
## Plot the rate of convergence
#plt.plot(range(1, 100), convergence_rate)
#plt.xlabel('Number of iterations')
#plt.ylabel('Rate of convergence')
#plt.title('Rate of Convergence of Newton-Raphson Method')
#plt.grid(True)
#plt.show()

#convergence = []
#for k in range(0, mp.dps):
#    term = bbp_term(k)
#    pi += term
#    convergence.append(abs(pi - mp.pi))

# Plot the convergence
#plt.plot(range(1, mp.dps + 1), convergence,label='Convergence of BBP series to Pi')
##plot a doted line in the value y = mp.pi
#plt.axhline(y=mp.pi, color='r', linestyle='dotted',label='mp.pi')
#plt.xlabel('Term')
#plt.ylabel('Approximated value of Pi')
#plt.title('Convergence of BBP series to Pi')
#plt.legend()
#plt.show()

