from mpmath import mp
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import random  

def randomwalk(m):
    rand = []
    distance = [0]
    step = 0
    average = 0
    countx = 0
    county = 0
    k = m+1
    x = np.zeros(k)
    y = np.zeros(k)
    for i in range(0,m):
        rand.append(random.randint(0,9)) 
    x[0] = 0
    y[0] = 0
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
        dx,dy = step_map[rand[i-1]]
        countx += dx
        county += dy
        x[i] = countx
        y[i] = county
        if rand[i-1] != 1 and rand[i-1] != 0:
            step +=1
            distance.append(np.sqrt(x[i]**2+y[i]**2))
    
    l = len(distance)
    for i in range(0,l):
        average += distance[i]

    average = average/step
    print(distance)
    print(average)
    print(step)

#    # create a figure
#    fig = plt.figure()
#    # create a plot into the figure
#    average = average/step
#    ax = fig.add_subplot(111)
#    ax.plot(distance)
#    plt.axhline(y=distance[-1], color='r', linestyle='-')
#    plt.title("Distance to the origin (d = {})".format(m))
#    ax.set_ylabel("Distance to the origin per step")
#    ax.set_xlabel("Step")
    return x,y


m = 10
x1,y1 = randomwalk(m)


# create a figure
fig = plt.figure()
# create a plot into the figure
ax1 = fig.add_subplot(111)

colors1 = np.linspace(0, 1, len(x1))
# plot the data
for i in range(1, len(x1)):
    ax1.plot([x1[i-1],x1[i]], [y1[i-1],y1[i]], color=plt.cm.viridis(colors1[i]))

# Add color bar with tick labels
cmap = plt.cm.viridis
norm = plt.Normalize(0, 1)
sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([]) # Dummy array for color mapping
cbar = plt.colorbar(sm, ax=ax1)
cbar.set_ticks([0, 1])
cbar.set_ticklabels(['Beginning', 'End'])

plt.title("Random-walk")

plt.show()


