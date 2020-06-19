from random import random
from random import seed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def random_walk_1D(start_pos_a, start_pos_b, steps, left_ratio, stationary_ratio=0):

    fig = plt.figure()
    axs = plt.axes()

    right_ratio = 1 - left_ratio - stationary_ratio

    random_walk_lst_1 = [start_pos_a]

    random_walk_lst_2 = [start_pos_b]

    move_increments = [-1, 0, 1]

    i = 1

    while i < (steps + 1):
        move_choice_1 = np.random.choice(move_increments, size=1, p=[
            left_ratio, stationary_ratio, right_ratio])

        move_choice_2 = np.random.choice(move_increments, size=1, p=[
            left_ratio, stationary_ratio, right_ratio])

        # calculate new pos based on previous iter
        new_val = random_walk_lst_1[i-1] + move_choice_1[0]
        random_walk_lst_1.append(new_val)

        new_val = random_walk_lst_2[i-1] + move_choice_2[0]
        random_walk_lst_2.append(new_val)

        i += 1

        if random_walk_lst_1[-1] == random_walk_lst_2[-1]:
            print(i)
            i = steps + 1

    #Distance_from_start_pos = random_walk_lst[-1] - random_walk_lst[0]

    xdata_a, ydata_a = [], []
    xdata_b, ydata_b = [], []

    ln, = plt.plot(xdata_a, ydata_a, color='blue')
    ln2, = plt.plot(xdata_b, ydata_b, color='red')

    def init():
        axs.set_xlim((start_pos_a - steps)/2, (start_pos_a + steps)/2)
        axs.set_ylim(0, steps)
        ln.set_data([], [])
        ln2.set_data([], [])
        return ln, ln2,

    def update(frame):
        xdata_a.append(random_walk_lst_1[int(frame)])
        ydata_a.append(int(frame))
        xdata_b.append(random_walk_lst_2[int(frame)])
        ydata_b.append(int(frame))
        ln.set_data(xdata_a, ydata_a)
        ln2.set_data(xdata_b, ydata_b)
        return ln, ln2,

    animate = FuncAnimation(fig, update, frames=np.linspace(0, len(
        random_walk_lst_1)-1, num=len(random_walk_lst_1)), interval=20, init_func=init, blit=True, repeat=False)

    plt.show()


random_walk_1D(0, -10, 200, .5)
