import matplotlib.pyplot as plt
import matplotlib.animation as a
import random as rnd

fig, ax = plt.subplot(1,1)
def animate(f):
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    colors = ["r", "b", "y", "g"]
    color = colors[rnd.randint(0, 3)]
    ax.plot(f,f, "o"+color)

def run():
    karen = a.FuncAnimation(fig, animate, frames = 10, interval= 1000)
    plt.show()

run()