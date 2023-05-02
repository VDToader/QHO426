import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
    print(frame)

def run():
    fig = plt.figure(fig, animate, interval = 1000, frames = 10)
    bob = animation.FuncAnimation()
    plt.show()

run()