import numpy as np
import random as random
import matplotlib.pyplot as plt
import math
from math import hypot


def in_radius(center_x, center_y, r, x, y):
    return math.hypot(center_x - x, center_y - y) <= r # root((center_x - x)^2 + (center_y - y)^2)


def random_walk(point):
    x = point[0]
    y = point[1]
    rand_num = random.random()
    if rand_num < 0.25:
        x += 1
    elif rand_num >= 0.25 and rand_num < 0.5:
        x += -1
    elif rand_num >= 0.5 and rand_num < 0.75:
        y += 1
    else:
        y += -1
    point[0] = x
    point[1] = y
    return point


for simulation_num in range(1, 11): # perform 10 plots
    r = 100
    # origin at (125, 125); i = [0, 250] j = [0, 250]

    # create lattice
    lattice = np.zeros((250, 250))
    lattice[125][125] = 1

    circle = []
    i = 0
    j = 0

    # create list of perimeter points
    for i in range(250):
        for j in range(250):
            radius = np.sqrt((125 - i) ** 2 + (125 - j) ** 2)
            # there is a little leeway (+/- 1) for creating the list of perimeter points to create a
            # large sampling of points at or near the perimeter. there were very few points that had a radius of
            # exactly 100, which leaves room for additional errors
            if radius < 101 and radius > 99:
                circle.append([i, j])

    elements_in_circle = len(circle)
    circle_index_max = elements_in_circle - 1

    isSize = False
    while isSize is False:
        # place new particle at random point along perimeter
        rand = random.randint(0, circle_index_max)
        point = circle[rand]
        x_old = (circle[rand])[0]
        y_old = (circle[rand])[1]
        lattice[x_old][y_old] = -1
        isAdded = False
        escape = False

        # check if adjacent points are occupied
        if x_old + 1 < 250 and y_old + 1 < 250 and x_old - 1 > 0 and y_old - 1 > 0:
            if lattice[x_old + 1][y_old] == 1:
                lattice[x_old][y_old] = 1
                isAdded = True
            elif lattice[x_old - 1][y_old] == 1:
                lattice[x_old][y_old] = 1
                isAdded = True
            elif lattice[x_old][y_old + 1] == 1:
                lattice[x_old][y_old] = 1
                isAdded = True
            elif lattice[x_old][y_old - 1] == 1:
                lattice[x_old][y_old] = 1
                isAdded = True
            else:
                lattice[x_old][y_old] = -1

        while isAdded is False:
            point = random_walk(point)
            x_new = point[0]
            y_new = point[1]
            if np.sqrt((x_new - 100) ** 2 + (y_new - 100) ** 2) > 101:
                escape = True
                lattice[x_new][y_new] = 0
                break
            else:
                lattice[x_new][y_new] = -1
                lattice[x_old][y_old] = 0

            # check if adjacent points are occupied
            if x_new + 1 < 250 and y_new + 1 < 250 and x_new - 1 > 0 and y_new - 1 > 0:
                if lattice[x_new + 1][y_new] == 1:
                    lattice[x_new][y_new] = 1
                    isAdded = True
                elif lattice[x_new - 1][y_new] == 1:
                    lattice[x_new][y_new] = 1
                    isAdded = True
                elif lattice[x_new][y_new + 1] == 1:
                    lattice[x_new][y_new] = 1
                    isAdded = True
                elif lattice[x_new][y_new - 1] == 1:
                    lattice[x_new][y_new] = 1
                    isAdded = True
                else:
                    lattice[x_new][y_new] = 0
                    point = [x_new, y_new]
                    x_old = x_new
                    y_old = y_new

        np.savetxt(str(simulation_num) + "_cluster.txt", lattice)
        # check is desired size is achieved
        if escape is False:
            for m in range(elements_in_circle):
                x = (circle[m])[0]
                y = (circle[m])[1]
                if lattice[x][y] == 1:
                    isSize = True

    np.savetxt(str(simulation_num) + "_cluster.txt", lattice)

    # create 2 arrays storing x and y positions of cluster points
    x = []
    y = []
    for i in range(250):
        for j in range(250):
            if lattice[i][j] == 1:
                x.append(i)
                y.append(j)

    plt.scatter(x, y, label="Cluster Particles")
    plt.xlabel("Horizontal Position")
    plt.ylabel("Vertical Position")
    plt.title("2D Cluster Growth Using the DLA Model")
    plt.legend()
    plt.savefig(str(simulation_num) + "_2DCluster.png")
    plt.show()

    to_plotr = []
    to_plotm = []
    cluster_parts = np.where(lattice == 1)
    for r in range(100):
        counter = 0
        for i in range(len(cluster_parts[0])):  # len(cluster_parts) len of row list coordinates
            if in_radius(125, 125, r, cluster_parts[0][i], cluster_parts[1][i]):
                counter += 1
        to_plotr.append(r)
        to_plotm.append(counter)

    plt.loglog(to_plotr, to_plotm)
    plt.title('Mass vs r')
    plt.ylabel('Mass')
    plt.xlabel('r')
    plt.savefig(str(simulation_num) + '_loglog clusters.png')
    plt.show()