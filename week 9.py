import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
#
# def animate(frame):
#     print(frame)
#
# def run():
#     fig, ax = plt.subplots()
#     simple_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
#     #fig, ax = plt.subplots()
#     plt.show()
#
# run()

# fig, ax = plt.subplots()
#
# def animate():
#     global ax
#     ax.set_xlim(0, 10)
#     ax.set_ylim(0, 10)
#     c=0
#     while c < 11:
#         xframe= c
#         yframe = c
#         ax.plot(xframe, yframe)
#         plot = plt.plot(xframe,yframe, 'ro')
#         simple_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
#         c=c+1
#         #time.sleep(2)
#     return plot
#
# def run():
#     global fig
#     animate()
#     plt.show()
#
# run()

# line = None
#
# def animate(frame):
#     global line
#     #line.set_data(range(frame), range(frame))
#
# def run():
#     global line
#     fig, ax = plt.subplots()
#     ax.set_xlim(0, 10)
#     ax.set_ylim(0, 10)
#     c=0
#     while c < 11:
#         xval = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         yval = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         xco = c in xval
#         yco = c in yval
#         #line, ax.plot([xco], [yco], 'ro')
#         plt.plot([xco], [yco], 'ro')
#         simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
#         c=c+1
#     plt.show()
#
# run()


import math

fig, ax = plt.subplots()

def animate(frame):
    global ax
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    x = range(0, frame)

    y = []
    for degrees in x:
        y.append(math.sin(math.radians(degrees)))



    ax.plot(x, y)

def run():
    global line
    sine_animation = animation.FuncAnimation( fig, animate, frames = 720, interval = 100)
    plt.show()

run()