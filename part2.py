import numpy as np
import random as random
import matplotlib.pyplot as plt

#control for grid dimensions
grid_size = 5

#declare arrays
fish_positions = [[-1 for j in range(grid_size)] for i in range(grid_size)]
shark_positions = [[-1 for j in range(grid_size)] for i in range(grid_size)]
fish_move = [[0 for j in range(grid_size)] for i in range(grid_size)]
shark_move = [[0 for j in range(grid_size)] for i in range(grid_size)]
shark_starve = [[0 for j in range(grid_size)] for i in range(grid_size)]
iter_array =  np.arange(0,grid_size,1)
time_steps = np.arange(1, 365, 1)


#Function to seed intial populations
def pop_seed(twoD_array, pop_Max):
    pop = 0
    while (pop < pop_Max):
        rand_int_i = random.randint(0, grid_size-1)
        rand_int_j = random.randint(0, grid_size-1)
        if (twoD_array[rand_int_i][rand_int_j] == 0):
            rand_int_i = random.randint(0, grid_size-1)
            rand_int_j = random.randint(0, grid_size-1)
            twoD_array[rand_int_i][rand_int_j] = 0
        else:
            twoD_array[rand_int_i][rand_int_j] = 0
        pop = pop + 1

#function to check and randomly choose an adjacent unoccupied location
def location_check_pick(twoD_array, max_size, x, y):
    loc = random.randint(1,4)
    if (loc == 1):
        if ((y-1) > -1):
            if twoD_array[x][max_size] > -1:
                location_check_pick(twoD_array, max_size, x, y)
            else:
                return "left"
        elif twoD_array[x][y-1] > -1:
            location_check_pick(twoD_array, max_size, x, y)
        else:
            return "left"
    elif (loc == 2):
        if ((x+1) > max_size):
            if twoD_array[0][y] > -1:
                location_check_pick(twoD_array, max_size, x, y)
            else:
                return "down"
        elif twoD_array[x+1][y] > -1:
                location_check_pick(twoD_array, max_size, x, y)
        else:
            return "down"
    elif (loc == 3):
        if ((y+1) > max_size):
            if twoD_array[x][0] > -1:
                location_check_pick(twoD_array, max_size, x, y)
            else:
                return "right"
        elif twoD_array[x][y] > -1:
                location_check_pick(twoD_array, max_size, x, y)
        else:
            return "right"


# for t in time_steps:
#     for i in iter_array:
#         for j in iter_array:
#            if fish_positions[i][j] != -1:


