import numpy as np
import random as random
import matplotlib.pyplot as plt

#parameter controls
grid_size = 5
fish_breed = 3

#declare arrays
fish_positions = [[-1 for j in range(grid_size)] for i in range(grid_size)]
shark_positions = [[-1 for j in range(grid_size)] for i in range(grid_size)]
shark_starve = [[0 for j in range(grid_size)] for i in range(grid_size)]
iter_array =  np.arange(0, grid_size, 1)
time_steps = np.arange(0, 5, 1)


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
    rand_loc = random.randint(0, length-1)

    if length == 0:
        new_row = x
        new_col = y
    else:
        if direction[rand_loc] == 'up':
            if ((x-1) < 0):
                new_row = max_size - 1
            else:
                new_row = x - 1
            new_col = y
        elif direction[rand_loc] == 'right':
            new_row = x
            if ((y + 1) > (max_size - 1)):
                new_col = 0
            else:
                new_col = y + 1
        elif direction[rand_loc] == 'down':
            if ((x + 1) > (max_size -1)):
                new_row = 0
            else:
                new_row = x + 1
            new_col = y
        elif direction[rand_loc] == 'left':
            new_row = x
            if ((y -1) < 0):
                new_col = max_size -1
            else:
                new_col = y - 1

    return new_row, new_col


def hunt_location_check_pick(twoD_array, max_size, x, y):
    direction = []

    if (x == 0):
        if twoD_array[max_size-1][y] >= 0:
            direction.append('up')
    elif twoD_array[x-1][y] >= 0:
        direction.append('up')

    if(y == max_size-1):
        if twoD_array[x][0] >= 0:
            direction.append('right')
    elif twoD_array[x][y+1] >= 0:
        direction.append('right')

    if (x == max_size - 1):
        if twoD_array[0][y] >= 0:
            direction.append('down')
    elif twoD_array[x+1][y] >= 0:
        direction.append('down')

    if (y == 0):
        if twoD_array[x][max_size-1] >= 0:
            direction.append('left')
    elif twoD_array[x][y - 1] >= 0:
        direction.append('left')

    length = len(direction)
    rand_loc = random.randint(0, length-1)

    if length == 0:
        new_row = x
        new_col = y
    else:
        if direction[rand_loc] == 'up':
            if ((x-1) < 0):
                new_row = max_size - 1
            else:
                new_row = x - 1
            new_col = y
        elif direction[rand_loc] == 'right':
            new_row = x
            if ((y + 1) > (max_size - 1)):
                new_col = 0
            else:
                new_col = y + 1
        elif direction[rand_loc] == 'down':
            if ((x + 1) > (max_size -1)):
                new_row = 0
            else:
                new_row = x + 1
            new_col = y
        elif direction[rand_loc] == 'left':
            new_row = x
            if ((y -1) < 0):
                new_col = max_size -1
            else:
                new_col = y - 1

    return new_row, new_col







pop_seed(fish_positions, 3)
pop_seed(shark_positions, 1)

for row in fish_positions:
    print(row)

print('')


for t in time_steps:
    fish_move = [[0 for j in range(grid_size)] for i in range(grid_size)]
    shark_move = [[0 for j in range(grid_size)] for i in range(grid_size)]
    for i in iter_array:
        for j in iter_array:
            # fish moving code
           if fish_positions[i][j] >= 0:
               if fish_move[i][j] == 0:
                   if fish_positions[i][j] == fish_breed:
                       move_i, move_j = location_check_pick(fish_positions, grid_size, i, j)
                       if move_i == i and move_j == j:
                           fish_positions[move_i][move_j] = 0
                           fish_move[move_i][move_j] = 1
                       else:
                           fish_positions[move_i][move_j] = 0
                           fish_move[move_i][move_j] = 1
                           fish_positions[i][j] = 0
                   else:
                        move_i, move_j = location_check_pick(fish_positions, grid_size, i, j)
                        if move_i == i and move_j == j:
                            fish_positions[move_i][move_j] = fish_positions[i][j] + 1
                            fish_move[move_i][move_j] = 1
                        else:
                            fish_positions[move_i][move_j] = fish_positions[i][j] + 1
                            fish_move[move_i][move_j] = 1
                            fish_positions[i][j] = -1

        ## shark code
        for j in iter_array:
            if shark_positions[i][j] >= 0:
                if shark_move[i][j] == 0:
                    s_move_i, s_move_j = hunt_location_check_pick(fish_positions, grid_size, i, j)
                    if s_move_i == i and s_move_j == j:
                        mv_shark_i, mv_shark_j = location_check_pick(shark_positions, grid_size, i, j)
                        if mv_shark_i == i and mv_shark_j == j:
                            shark_positions[mv_shark_i][mv_shark_j] = shark_positions[i][j] + 1
                            shark_move[mv_shark_i][mv_shark_j] = 1
                        else:
                            shark_positions[mv_shark_i][mv_shark_j] = shark_positions[i][j] + 1
                            shark_move[mv_shark_i][mv_shark_j] = 1
                            shark_positions[i][j] = -1
                    else:
                        shark_positions[s_move_i][s_move_j] = shark_positions[i][j] + 1
                        shark_positions[i][j] = -1
                        shark_move[s_move_i][s_move_j] = 1
                        fish_positions[s_move_i][s_move_j] = -1


    for row in fish_positions:
        print(row)
    print('')
