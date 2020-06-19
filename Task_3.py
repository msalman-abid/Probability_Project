from random import random
from random import seed
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def discrete_random_variable(start_pos: tuple, steps, radius=100):

    fig = plt.figure()
    axs = plt.axes()

    circle1 = plt.Circle((0,0), radius, color='r', alpha=0.2)

    axs.add_artist(circle1)

    random_walk_lst = [start_pos]

    move_increments = [0, 0.5, 1]
    angle_increments = []
    current_pos = tuple()

    # orientation with 45 degree increments
    # for x in range(9):
    #     angle_increments.append(int(45*x))

    for x in range(0, 361):
        angle_increments.append(int(x))

    # print(angle_increments)

    for i in range(1, steps):

        move_choice = np.random.choice(move_increments)

        angle_choice = np.random.choice(angle_increments)

        last_pos = random_walk_lst[-1]

        x_temp, y_temp = get_xy(move_choice, angle_choice)

        current_pos = last_pos[0] + \
            x_temp, last_pos[1] + y_temp

        if(check_collision(radius, current_pos, last_pos)):

            intersection_pt = find_intersection(
                radius, last_pos, start_pos, x_temp, y_temp)

            
            AB = (intersection_pt[0] - last_pos[0],
                  intersection_pt[1] - last_pos[1])

            # if get_magnitude(AB) == 0.0:
            #     print("magnitude : 0, continued")
            #     last_pos = random_walk_lst[-2]
            #     continue

            angle_collision = math.acos((AB[0] * intersection_pt[0] + AB[1] * intersection_pt[1]) / (
                get_magnitude(AB) * get_magnitude(intersection_pt)))


            angle_rebound = 180 - angle_collision

            x_temp, y_temp = get_xy(move_choice, angle_rebound)
            
            current_pos = last_pos[0] + \
                x_temp, last_pos[1] + y_temp

        if math.sqrt((current_pos[0])**2 + (current_pos[1] ** 2)) >= radius:
            continue
        random_walk_lst.append(current_pos)

    #print(random_walk_lst)

    xdata, ydata = [], []
    ln, = plt.plot(xdata, ydata, color='green')
    print(type(ln))

    def init():
        axs.set_xlim(start_pos[0] - radius - 10, start_pos[0] + radius + 10)
        axs.set_ylim(start_pos[1] - radius - 10, start_pos[1] + radius + 10)
        ln.set_data([], [])
        return ln,

    def update(frame):
        xdata.append(random_walk_lst[int(frame)][0])
        ydata.append(random_walk_lst[int(frame)][1])
        ln.set_data(xdata, ydata)
        return ln,
    ani = FuncAnimation(fig, update, frames=np.linspace(0, len(random_walk_lst)-1, num=len(random_walk_lst)), interval=5,
                        init_func=init, blit=True, repeat=False)

    plt.show()


def get_xy(hypt: int, theta: int):
    xy = (math.cos(theta) * hypt, math.sin(theta) * hypt)
    return xy


def check_collision(radius: int, pos_tuple: tuple, last_pos: tuple):
    if (math.sqrt((pos_tuple[0])**2 + (pos_tuple[1] ** 2))) >= radius:
        return True
    else:
        return False


def find_intersection(radius: int, pos_tuple: tuple, start_pos: tuple, x_incr, y_incr):
    temp_pos = [pos_tuple[0], pos_tuple[1]]
    slice_ = 1000

    while (not check_collision(radius, tuple(temp_pos), start_pos)):
        temp_pos[0] += (x_incr/slice_)
        temp_pos[1] += (y_incr/slice_)
    
    temp_pos[0] -= (x_incr/slice_)
    temp_pos[1] -= (y_incr/slice_)

    return temp_pos


def get_magnitude(x: tuple):
    return math.sqrt(x[0] ** 2 + x[1] ** 2)


discrete_random_variable((0, 0), 3000)
