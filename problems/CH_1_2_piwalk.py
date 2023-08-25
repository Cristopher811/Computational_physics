from mpmath import mp
import matplotlib.pyplot as plt
import numpy 

x = numpy.arange(0, 1, 0.05)
y = numpy.power(x, 2)

fig = plt.figure
ax = fig.gca()
ax.set_xticks(numpy.arange(0, 1, 0.1))
ax.set_yticks(numpy.arange(0, 1., 0.1))
plt.scatter(x, y)
plt.grid()
plt.show()


# Set the desired precision
mp.dps = 1000
# Get the value of pi
pi_value = mp.pi
