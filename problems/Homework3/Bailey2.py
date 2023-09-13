from mpmath import mp
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import mynrmethod as nr

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

n_ite = 10**3
# Calculate the value of pi using BBP series
def calculate_pi():
    pi = mp.mpf(0)
    pi_value = []
    for k in range(0, n_ite):
        pi += bbp_term(k)
        pi_value.append(pi)
    return pi_value

# convergence of BBP series
pi_value = calculate_pi()
convergencebbp = []
for i in range(0,n_ite):
    convergencebbp.append(mp.fabs(mp.pi-pi_value[i]))

# convergence of NR method
values = []
ite = []
convergencenr = []

values = nr.pi(4,n_ite,1e-1200)[1]
ite = nr.pi(4,n_ite,1e-1200)[0]

for i in range(0,len(ite)):
    convergencenr.append(mp.fabs(mp.pi-values[i]))


# Plot the rate of convergence
plt.plot(range(0, n_ite), convergencebbp,label='BBP convergence rate')
plt.plot(range(0,n_ite), convergencenr,label='NR convergence rate')
plt.yscale("log")
plt.xscale("log")
plt.xlabel('Number of iterations')
plt.ylabel('Error')
plt.title('Rate of Convergence to $\pi$')
plt.grid(True)
plt.legend()
plt.show()
