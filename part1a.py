import numpy as np
import random as random
import matplotlib.pyplot as plt

def check_adjacent(lattice, point):
    x = point[0]
    y = point[1]
    if x + 1 < 250 and y + 1 < 250 and x - 1 > 0 and y - 1 > 0:
        if lattice[x + 1][y] == 1:
            lattice[x][y] = 1
        elif lattice[x - 1][y] == 1:
            lattice[x][y] = 1
        elif lattice[x][y + 1] == 1:
            lattice[x][y] = 1
        elif lattice[x][y - 1] == 1:
            lattice[x][y] = 1
        else:
            lattice[x][y] = -1
    return lattice


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
        radius = np.sqrt((125-i)**2 + (125-j)**2)
        if radius < 101 and radius > 99:
            circle.append([i, j])

print(circle)
elements_in_circle = len(circle)
circle_index_max = elements_in_circle - 1


isSize = False
while isSize is False:
    # place new particle at random point along perimeter
    rand = random.randint(0, circle_index_max)
    print(rand)
    point = circle[rand]
    x_old = (circle[rand])[0]
    y_old = (circle[rand])[1]
    lattice[x_old][y_old] = -1
    isAdded = False
    escape = False

    # check if adjacent points are occupied
    for i in range(250):
        for j in range(250):
            lattice[i][j] = (check_adjacent(lattice, point))[i][j]
    if lattice[x_old][y_old] == 1:
        isAdded = True

    while isAdded is False:
        point = random_walk(point)
        x_new = point[0]
        y_new = point[1]
        if np.sqrt((x_new - 100) ** 2 + (y_new - 100) ** 2) > 101:
            escape = True
            lattice[x_new][y_new] = 0
            break
        lattice[x_new][y_new] = -1
        lattice[x_old][y_old] = 0

        # check if adjacent points are occupied
        for i in range(250):
            for j in range(250):
                lattice[i][j] = (check_adjacent(lattice, point))[i][j]
        if lattice[x_old][y_old] == 1:
            isAdded = True
        else:
            x_old = x_new
            y_old = y_new
            point = [x_old, y_old]

    np.savetxt("cluster.txt", lattice)
    # check is desired size is achieved
    if escape is False:
        for m in range(elements_in_circle):
            x = (circle[m])[0]
            y = (circle[m])[1]
            if lattice[x][y] == 1:
                isSize = True

np.savetxt("cluster.txt", lattice)

x = []
y = []
for i in range(250):
    for j in range(250):
        if lattice[i][j] == 1:
            x.append(i)
            y.append(j)

plt.scatter(x, y)
plt.show()

