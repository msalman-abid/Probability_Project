from random import random
from random import seed
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from statistics import mean


def task_8(start_pos: tuple, radius=100):

    radius = 100
    fig = plt.figure()
    axs = plt.axes()

    circle1 = plt.Circle(start_pos, radius, color='r', alpha=0.2)

    axs.add_artist(circle1)

    pt1_r, pt2_r = np.random.uniform (high=100.0, size=2)
    pt1_angle, pt2_angle = np.random.uniform (high=360.0, size=2)

    start_pos1 = get_full_coord(pt1_r, pt1_angle)
    start_pos2 = get_full_coord(pt2_r, pt2_angle)

    random_walk_n1 = [start_pos1]
    random_walk_n2 = [start_pos2]

    move_increments = [0, 0.5, 1]
    current_pos1 = tuple()
    current_pos2 = tuple()

    # print(angle_increments)
    counter = 0

    while (True):

        counter += 1
        move_choice1 = np.random.choice(move_increments)
        angle_choice1 = np.random.uniform(high=360.0)

        last_pos1 = random_walk_n1[-1]
        last_pos2 = random_walk_n2[-1]

        x_temp1, y_temp1 = get_xy(move_choice1, angle_choice1)

        move_choice2 = np.random.choice(move_increments)
        angle_choice2 = np.random.uniform(high=360.0)

        x_temp2, y_temp2 = get_xy(move_choice2, angle_choice2)

        current_pos1 = last_pos1[0] + \
            x_temp1, last_pos1[1] + y_temp1

        current_pos2 = last_pos2[0] + \
            x_temp2, last_pos2[1] + y_temp2

        if(check_collision(radius, current_pos1)):

            intersection_pt = find_intersection(
                radius, last_pos1, x_temp1, y_temp1)

            AB = (intersection_pt[0] - last_pos1[0],
                  intersection_pt[1] - last_pos1[1])

            if get_magnitude(AB) == 0.0:
                continue

            angle_collision = math.acos((AB[0] * intersection_pt[0] + AB[1] * intersection_pt[1]) / (
                get_magnitude(AB) * get_magnitude(intersection_pt)))

            angle_rebound = 180 - angle_collision

            x_temp1, y_temp1 = get_xy(move_choice1, angle_rebound)

            current_pos1 = last_pos1[0] + \
                x_temp1, last_pos1[1] + y_temp1

            if math.sqrt((current_pos1[0])**2 + (current_pos1[1] ** 2)) >= radius:
                continue

        if(check_collision(radius, current_pos2)):

            intersection_pt = find_intersection(
                radius, last_pos2, x_temp2, y_temp2)

            AB = (intersection_pt[0] - last_pos2[0],
                  intersection_pt[1] - last_pos2[1])

            if get_magnitude(AB) == 0.0:
                continue

            angle_collision = math.acos((AB[0] * intersection_pt[0] + AB[1] * intersection_pt[1]) / (
                get_magnitude(AB) * get_magnitude(intersection_pt)))

            angle_rebound = 180 - angle_collision

            x_temp2, y_temp2 = get_xy(move_choice2, angle_rebound)

            current_pos2 = last_pos2[0] + \
                x_temp2, last_pos2[1] + y_temp2

            if math.sqrt((current_pos2[0])**2 + (current_pos2[1] ** 2)) >= radius:
                continue

        random_walk_n1.append(current_pos1)
        random_walk_n2.append(current_pos2)

        if within_range(random_walk_n1[-1], random_walk_n2[-1]):
            break
    # print(random_walk_lst)

    xdata1, ydata1 = [], []
    xdata2, ydata2 = [], []

    ln1, = plt.plot(xdata1, ydata1, color='green')
    ln2, = plt.plot(xdata2, ydata2, color='blue')

    def init():
        axs.set_xlim(start_pos[0] - radius - 10, start_pos[0] + radius + 10)
        axs.set_ylim(start_pos[1] - radius - 10, start_pos[1] + radius + 10)
        ln1.set_data([], [])
        ln2.set_data([], [])

        return ln1, ln2,

    def update(frame):
        xdata1.append(random_walk_n1[int(frame)][0])
        ydata1.append(random_walk_n1[int(frame)][1])
        ln1.set_data(xdata1, ydata1)

        xdata2.append(random_walk_n2[int(frame)][0])
        ydata2.append(random_walk_n2[int(frame)][1])
        ln2.set_data(xdata2, ydata2)
        return ln1, ln2,

    max_final = max(len(random_walk_n1), len(random_walk_n2))

    ani = FuncAnimation(fig, update, frames=np.linspace(0, (max_final)-1, num=(max_final)), interval=5,
                        init_func=init, blit=True, repeat=False)

    print("test", counter)
    plt.show()
    # return counter


def get_xy(hypt: int, theta: int):
    xy = (math.cos(theta) * hypt, math.sin(theta) * hypt)
    return xy


def check_collision(radius: int, pos_tuple: tuple):
    # checking radius against (x^2 + y^2) ^ 0.5
    if (math.sqrt((pos_tuple[0])**2 + (pos_tuple[1] ** 2))) >= radius:
        return True
    else:
        return False


def find_intersection(radius: int, pos_tuple: tuple, x_incr, y_incr):
    temp_pos = [pos_tuple[0], pos_tuple[1]]

    while (not check_collision(radius, tuple(temp_pos))):
        temp_pos[0] += (x_incr/1000)
        temp_pos[1] += (y_incr/1000)

    temp_pos[0] -= (x_incr/1000)
    temp_pos[1] -= (y_incr/1000)

    return temp_pos


def get_magnitude(x: tuple):
    return math.sqrt(x[0] ** 2 + x[1] ** 2)


def get_full_coord(radius, angle):
    x_coord = radius * math.cos(angle)
    y_coord = radius * math.sin(angle)

    return x_coord, y_coord


def within_range(pos_1: tuple, pos_2: tuple):
    dist = math.sqrt((pos_2[0] - pos_1[0])**2 + (pos_2[1] - pos_1[1])**2)
    return True if dist <= 1 else False

# def main():
#     baap_lst = list()

#     for x in range(100001):
#         y = task_8(0,0)
#         baap_lst.append(y)

#     print("working")
#     print(mean(baap_lst))
#     print("length of list:", len(baap_lst))
#     return 0


# main()
task_8((0, 0))
