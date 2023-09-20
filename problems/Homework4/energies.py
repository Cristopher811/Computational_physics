import matplotlib.pyplot as plt
import numpy as np

odd_energies = [7.000002433254849,2.9999999884166755]
even_energies = [9.000025350542273, 5.000000213331077, 0.999999959662091]
energies = even_energies + odd_energies

#sort energies in ascending order
energies.sort()

x = np.linspace(0,4,5)
print(x)

# plot even energies as scatter points
plt.scatter(x,energies)
plt.xlabel('bound state')
plt.ylabel('energy')
plt.show()
