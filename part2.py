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
time_steps = np.arange(1, 5, 1)


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
    direction = ['up', 'right', 'down', 'left']

    if (x == 0):
        if twoD_array[max_size-1][y] >= 0:
            direction.remove('up')
    elif twoD_array[x-1][y] >= 0:
        direction.remove('up')

    if(y == max_size-1):
        if twoD_array[x][0] >= 0:
            direction.remove('right')
    elif twoD_array[x][y+1] >= 0:
        direction.remove('right')

    if (x == max_size - 1):
        if twoD_array[0][y] >= 0:
            direction.remove('down')
    elif twoD_array[x+1][y] >= 0:
        direction.remove('down')

    if (y == 0):
        if twoD_array[x][max_size-1] >= 0:
            direction.remove('left')
    elif twoD_array[x][y - 1] >= 0:
        direction.remove('left')

    length = len(direction)
    rand_loc = random.randint(0, length)

    if length == 0:
        new_row = x
        new_col = y
    else:
        if direction[rand_loc] == 'up':
            if (x-1 < 0):
                new_row = max_size -1
            else:
                new_row = x - 1
            new_col = y
        elif direction[rand_loc] == 'right':
            new_row = x
            if (y + 1 > max_size - 1):
                new_col = 0
            else:
                new_col = y + 1
        elif direction[rand_loc] == 'down':
            if (x + 1 > max_size -1):
                new_row = 0
            else:
                new_row = x + 1
            new_col = y
        elif direction[rand_loc] == 'left':
            new_row = x
            if (y -1 < 0):
                new_col = max_size -1
            else:
                new_col = y - 1
    return new_row, new_col

pop_seed(fish_positions, 2)

for row in fish_positions:
    print(row)

print('')

pot_change = 0

for t in time_steps:
    for i in iter_array:
        for j in iter_array:
           if fish_positions[i][j] >= 0:
                move_i, move_j = location_check_pick(fish_positions, grid_size, i, j)
                if move_i == i and move_j == j:
                    fish_positions[move_i][move_j] = fish_positions[i][j] + 1
                else:
                    fish_positions[move_i][move_j] = fish_positions[i][j] + 1
                    fish_positions[i][j] = -1
                pot_change = pot_change + 1
    for row in fish_positions:
        print(row)
    print(pot_change)