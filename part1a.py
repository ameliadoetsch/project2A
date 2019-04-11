import numpy as np
import random as random
import matplotlib.pyplot as plt

r = 100
# origin at (100, 100); i = [0, 200] j = [0, 200]

# create lattice
lattice = np.zeros((200, 200))
lattice[100][100] = 1

perimeter = []
# create list of perimeter points
for i in range(200):
    for j in range(200):
        if np.sqrt((i-100)**2 + (j-100)**2) == 100:
            perimeter.append([i, j])

elements_in_perimeter = len(perimeter)

isSize = False
while(isSize is False):
    # place new particle at random point along perimeter
    rand = random.randint(0, elements_in_perimeter)
    lattice[(perimeter[rand])[0]][(perimeter[rand])[1]] = -1
    location_old = perimeter[rand]

    # perform random walk
    isAdded = False
    while(isAdded is False):
        rand = random.random()
        if rand <= 0.25:
            if lattice[location_old[0] + 1][location_old[1]] == 1:
                break
            location_new = [location_old[0] + 1, location_old[1]]
        elif rand > 0.25 and rand <= 0.5:
            if lattice[location_old[0] - 1][location_old[1]] == 1:
                break
            location_new = [location_old[0] - 1, location_old[1]]
        elif rand > 0.5 and rand <= 0.75:
            if lattice[location_old[0]][location_old[1] + 1] == 1:
                break
            location_new = [location_old[0], location_old[1] + 1]
        else:
            if lattice[location_old[0]][location_old[1] - 1] == 1:
                break
            location_new = [location_old[0], location_old[1] - 1]

        lattice[location_new[0]][location_new[1]] = -1
        lattice[location_old[0]][location_old[1]] = 0

        if lattice[location_new[0] + 1][location_new[1]] == 1 or lattice[location_new[0] - 1][location_new[1]] == 1 or lattice[location_new[0]][location_new[1] + 1] == 1 or lattice[location_new[0]][location_new[1] - 1] == 1:
            lattice[location_new[0]][location_new[1]] = 1
            isAdded = True
        elif np.sqrt((location_new[0] - 100)**2 + (location_new[1] - 100)**2) > 100:
            break
        else:
            location_old[0] = location_new[0]
            location_old[1] = location_new[1]

    # check is desired size is achieved
    for m in range(elements_in_perimeter):
        if lattice[(perimeter[m])[0]][(perimeter[m])[0]] == 1:
            isSize = True

np.savetxt("cluster.txt", lattice)

x = []
y = []
for i in range(200):
    for j in range(200):
        if lattice[i][j] == 1:
            x.append(i)
            y.append(j)

plt.scatter(x, y)
plt.show()

