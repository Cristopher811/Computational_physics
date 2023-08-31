from mpmath import mp
import math
import matplotlib.pyplot as plt
import numpy as np
import random  
from matplotlib.animation import FuncAnimation



def lstdigits(n):
    n = str(n)
    if '.' in n:
      n = n.replace('.','')
    digits = list(n)
    digits = [int(i) for i in digits]
    return digits


def piwalk(n,m):
    digits = lstdigits(n)
    x = np.zeros(len(digits))
    y = np.zeros(len(digits))
    countx = 0
    county = 0
    total_steps = 0
    x[0] = countx
    y[0] = county



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
    for i in range(1,m):
        dx,dy = step_map[digits[i]]
        countx += dx
        county += dy
        total_steps += 1
        x[i] = countx
        y[i] = county
    return x,y

#def piwalk(n,m):
#    digits = lstdigits(n)
#    x = np.zeros(len(digits))
#    y = np.zeros(len(digits))
#    countx = 0
#    county = 0
#    s = 0
#    x[0] = countx
#    y[0] = county
#    for i in range(1,m):
#        if digits[i] == 0 or digits[i] == 1:
#            x[i] = countx
#            y[i] = county
#        if digits[i] == 2 or digits[i] == 3:
#            x[i] = countx+1
#            y[i] = county
#            countx+=1
#            s+=1
#        elif digits[i] == 4 or digits[i] == 5:
#            x[i] = countx
#            y[i] = county + 1
#            county+=1
#            s+=1
#        elif digits[i] == 6 or digits[i] == 7:
#            x[i] = countx - 1
#            y[i] = county
#            countx-=1
#            s+=1
#        elif digits[i] == 8 or digits[i] == 9:
#            x[i] = countx
#            y[i] = county - 1
#            county-=1
#            s+=1
##    distance = math.sqrt(x[m-1]**2 + y[m-1]**2)/s
##    print('Pi euclidean distances to the point: ',distance)
##    print('Pi step distance: ',s)
#    return x,y

def randomwalk(m):
    rand = []
    countx = 0
    county = 0
    x = np.zeros(m)
    y = np.zeros(m)
    s = 0
    for i in range(0,m):
        rand.append(random.randint(0,9)) 
    for i in range(0,m):
        if rand[i] == 0 or rand[i] == 1:
            x[i] = countx
            y[i] = county
        if rand[i] == 2 or rand[i] == 3:
            x[i] = countx+1
            y[i] = county
            countx+=1
            s+=1
        elif rand[i] == 4 or rand[i] == 5:
            x[i] = countx
            y[i] = county + 1
            county+=1
            s+=1
        elif rand[i] == 6 or rand[i] == 7:
            x[i] = countx - 1
            y[i] = county
            countx-=1
            s+=1
        elif rand[i] == 8 or rand[i] == 9:
            x[i] = countx
            y[i] = county - 1
            county-=1
            s+=1
    distance = math.sqrt(x[m-1]**2+y[m-1]**2)/s
    print('Random euclidean distances to the point: ',distance)
    print('Random step distance: ',s)
    return x,y


def update_color_gradient(ax, x, y,colors):
    ax.clear()

    num_points = len(x)
    for i in range(num_points-1):
        ax.plot([x[i], x[i+1]], [y[i], y[i+1]], '-o',color = colors[i])
    plt.draw()
    plt.pause(0.00000000001)


m = 10**4

mp.dps = m
n = mp.pi

#print(lstdigits(n))
x,y = piwalk(n,m)

# create a figure
fig = plt.figure()
# create a plot into the figure
ax = fig.add_subplot(111)

colors = np.linspace(0, 1, len(x))

# Plot the graph with a color gradient
for i in range(1, len(x)):
    ax.plot([x[i-1],x[i]], [y[i-1],y[i]], color=plt.cm.viridis(colors[i]))


#num_points = len(x)
#colors = [plt.cm.plasma(i / num_points) for i in range(num_points-1)]
#for i in range(1, m+1):
#    update_color_gradient(ax, x[:i], y[:i],colors[:i])
 
#plot the data

#animation = FuncAnimation(fig, lambda i: update_color_gradient(i, ax, x, y), frames=m, interval=10)
#animation.save('animation3.mp4', dpi=80, writer='ffmpeg')

#ax.plot(x,y)


#x1,y1 = randomwalk(m)
## create a figure
#fig = plt.figure()
## create a plot into the figure
#ax1 = fig.add_subplot(111)
## plot the data
#ax1.plot(x1,y1)
plt.show()

