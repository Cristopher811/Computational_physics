from mpmath import mp
import matplotlib.pyplot as plt
import numpy as np
from bokeh.plotting import figure, show

def lstdigits(n):
    n = str(n)
    if '.' in n:
      n = n.replace('.','')
    digits = list(n)
    digits = [int(i) for i in digits]
    return digits

def update_color_gradient_bokeh(p, x, y, colors):
    """
    Updates the plot with a color gradient based on the walk steps using Bokeh.

    Args:
        p: The Bokeh plot object.
        x: The x-coordinates of the walk.
        y: The y-coordinates of the walk.
        colors: The pre-calculated list of colors.
    """
    p.line(x, y, color=colors[-1])
    show(p)

def update_color_gradient(ax, x, y, colors):

    """
    Updates the plot with a color gradient based on the walk steps.

    Args:
        ax: The plot object.
        x: The x-coordinates of the walk.
        y: The y-coordinates of the walk.
        colors: The pre-calculated list of colors.
    """
    ax.clear()

    num_points = len(x)
    for i in range(num_points-1):
        ax.plot([x[i], x[i+1]], [y[i], y[i+1]], '-o', color=colors[i])

    plt.draw()


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



#def update_color_gradient(ax, x, y):
#    ax.clear()
#
#    num_points = len(x)
#    colors = [plt.cm.plasma(i / num_points) for i in range(num_points-1)]
#    for i in range(1, m+1):
#        update_color_gradient(ax,x[:i], y[:i], colors[:i])
#
#    plt.draw()
##    plt.pause(0.0001)


m = 10**2

mp.dps = m
n = mp.pi

x,y = piwalk(n,m)
#
## create a figure
fig = plt.figure()
## create a plot into the figure
ax = fig.add_subplot(111)


p = figure(title="Pi Random Walk", width=800, height=800)
num_points = len(x)
colors = [plt.cm.plasma(i / num_points) for i in range(num_points-1)]
for i in range(1, m+1):
    update_color_gradient(ax, x[:i], y[:i],colors[:i])
 
#plot the data

#animation = FuncAnimation(fig, lambda i: update_color_gradient(i, ax, x, y), frames=m, interval=10)
#animation.save('animation3.mp4', dpi=80, writer='ffmpeg')

#ax0.plot(x,y)


#x1,y1 = randomwalk(m)
## create a figure
#fig = plt.figure()
## create a plot into the figure
#ax1 = fig.add_subplot(111)
## plot the data
#ax1.plot(x1,y1)
#plt.show()

