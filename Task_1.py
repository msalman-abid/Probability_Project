from random import random
from random import seed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def random_walk_1D(start_pos, steps, left_ratio, stationary_ratio=0):

    fig = plt.figure()
    axs = plt.axes()

    right_ratio = 1 - left_ratio - stationary_ratio

    random_walk_lst = [start_pos]

    move_increments = [-1, 0, 1]

    for i in range(1, steps):

        move_choice = np.random.choice(move_increments, size=1, p=[
            left_ratio, stationary_ratio, right_ratio])

        # calculate new pos based on previous iter
        new_val = random_walk_lst[i-1] + move_choice[0]

        random_walk_lst.append(new_val)

    Distance_from_start_pos = random_walk_lst[-1] - random_walk_lst[0]

    xdata, ydata = [], []
    ln, = plt.plot(xdata, ydata, color='green')
    print(type(ln))

    def init():
        axs.set_xlim((start_pos - steps)/2, (start_pos + steps)/2)
        axs.set_ylim(0, steps)
        ln.set_data([], [])
        return ln,

    def update(frame):
        xdata.append(random_walk_lst[int(frame)])
        ydata.append(int(frame))
        ln.set_data(xdata, ydata)
        return ln,
    ani = FuncAnimation(fig, update, frames=np.linspace(0, len(random_walk_lst)-1, num=len(random_walk_lst)), interval=20,
                        init_func=init, blit=True, repeat=False)

    plt.show()


random_walk_1D(0, 100, .5)
