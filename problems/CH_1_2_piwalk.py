from mpmath import mp
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import random  

def lstdigits(n):
    n = str(n)
    if '.' in n:
      n = n.replace('.','')
    digits = list(n)
    digits = [int(i) for i in digits]
    return digits


def piwalk(n,m):
    digits = lstdigits(n)
    k = m+1
    x = np.zeros(k)
    y = np.zeros(k)
    countx = 0
    county = 0
    total_steps = 0
    x[0] = countx
    y[0] = county
    distance = [0]

    step_map = {
        0: (0, 0),
        1: (0, 0),
        2: (1, 0),
        3: (1, 0),
        4: (0, 1),
        5: (0, 1),
        6: (-1, 0),
        7: (-1, 0),
        8: (0, -1),
        9: (0, -1),
    }
    for i in range(1,k):
        dx,dy = step_map[digits[i-1]]
        countx += dx
        county += dy
        x[i] = countx
        y[i] = county
        if digits[i-1] != 1 and digits[i-1] != 0:
            distance.append(np.sqrt(x[i]**2+y[i]**2))
    # create a figure
    fig = plt.figure()
    # create a plot into the figure
    ax = fig.add_subplot(111)

    ax.set_xlabel('Step')
    ax.set_ylabel('Average distance')

    ax.plot(distance)
    return x,y

m = 10**3

mp.dps = m
n = mp.pi

x,y = piwalk(n,m)

# create a figure
fig = plt.figure()
# create a plot into the figure
ax = fig.add_subplot(111)

colors = np.linspace(0, 1, len(x))

# Plot the graph with a color gradient
for i in range(1, len(x)):
    ax.plot([x[i-1],x[i]], [y[i-1],y[i]], color=plt.cm.viridis(colors[i]))


# Add color bar with tick labels
cmap = plt.cm.viridis
norm = plt.Normalize(0, 1)
sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([]) # Dummy array for color mapping
cbar = plt.colorbar(sm, ax=ax)
cbar.set_ticks([0, 1])
cbar.set_ticklabels(['Beginning', 'End'])

plt.title("Pi-walk")
plt.show()

