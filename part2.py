import numpy as np
import random as random
import matplotlib.pyplot as plt

#parameter controls
grid_size = 50    #Size of grid
fish_breed = 6    #Fish breeding age
shark_breed = 10   #Shark breeding age
starve_age = 9   #Shark starvation age
fish_start = 2000   #Starting population of fish
shark_start = 500   #Starting population of sharks
n = 500           #Number of time steps


#declare variables
fish_positions = [[-1 for j in range(grid_size)] for i in range(grid_size)]
shark_positions = [[-1 for j in range(grid_size)] for i in range(grid_size)]
shark_starve = [[-1 for j in range(grid_size)] for i in range(grid_size)]
iter_array = np.arange(0, grid_size, 1)
time_steps = np.arange(0, n, 1)



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
    if length > 1:
        rand_loc = random.randint(0, length - 1)
    elif length == 1:
        rand_loc = 0

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

    if (x == 0) and y != 0:
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

    if (y == 0) and x != 0:
        if twoD_array[x][max_size-1] >= 0:
            direction.append('left')
    elif twoD_array[x][y - 1] >= 0:
        direction.append('left')


    length = len(direction)
    if length > 1:
        rand_loc = random.randint(0, length-1)
    elif length == 1:
        rand_loc = 0

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







pop_seed(fish_positions, fish_start)
pop_seed(shark_positions, shark_start)

fish_pop = []
shark_pop = []


for t in time_steps:
    fish = 0
    sharks = 0
    for i in iter_array:
        for j in iter_array:
            if fish_positions[i][j] >= 0:
                fish = fish + 1
            if shark_positions[i][j] >= 0:
                sharks =  sharks + 1
    fish_pop.append(fish)
    shark_pop.append(sharks)
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
                    if shark_starve[i][j] == starve_age:
                        shark_positions[i][j] = -1
                        shark_starve[i][j] = -1
                    else:
                        s_move_i, s_move_j = hunt_location_check_pick(fish_positions, grid_size, i, j)
                        if s_move_i == i and s_move_j == j:
                            mv_shark_i, mv_shark_j = location_check_pick(shark_positions, grid_size, i, j)
                            if mv_shark_i == i and mv_shark_j == j:
                                if shark_positions[i][j] == shark_breed:
                                    shark_positions[mv_shark_i][mv_shark_j] = 0
                                    shark_move[mv_shark_i][mv_shark_j] = 1
                                    shark_starve[mv_shark_i][mv_shark_j] = 0
                                else:
                                    shark_positions[mv_shark_i][mv_shark_j] = shark_positions[i][j] + 1
                                    shark_move[mv_shark_i][mv_shark_j] = 1
                                    shark_starve[mv_shark_i][mv_shark_j] = shark_starve[i][j] + 1
                            else:
                                if shark_positions[i][j] == shark_breed:
                                    shark_positions[mv_shark_i][mv_shark_j] = 0
                                    shark_move[mv_shark_i][mv_shark_j] = 1
                                    shark_positions[i][j] = 0
                                    shark_starve[mv_shark_i][mv_shark_j] = shark_starve[i][j] + 1
                                    shark_starve[i][j] = 0
                                else:
                                    shark_positions[mv_shark_i][mv_shark_j] = shark_positions[i][j] + 1
                                    shark_move[mv_shark_i][mv_shark_j] = 1
                                    shark_positions[i][j] = -1
                                    shark_starve[mv_shark_i][mv_shark_j] = shark_starve[i][j] + 1
                                    shark_starve[i][j] = -1
                        else:
                            if shark_positions[i][j] == shark_breed:
                                shark_positions[s_move_i][s_move_j] = 0
                                shark_positions[i][j] = 0
                                shark_move[s_move_i][s_move_j] = 1
                                fish_positions[s_move_i][s_move_j] = -1
                                shark_starve[s_move_i][s_move_j] = 0
                                shark_starve[i][j] = -1
                            else:
                                shark_positions[s_move_i][s_move_j] = shark_positions[i][j] + 1
                                shark_positions[i][j] = -1
                                shark_move[s_move_i][s_move_j] = 1
                                fish_positions[s_move_i][s_move_j] = -1
                                shark_starve[s_move_i][s_move_j] = 0
                                shark_starve[i][j] = -1
    # if ((t % 25 == 0) and t < 300) or t == 0:
    #     plt.figure(t)
    #     plt.subplot(2,1,1)
    #     plt.contourf(fish_positions)
    #     plt.title("Fish Age Density")
    #
    #     plt.subplot(2,1,2)
    #     plt.contourf(shark_positions)
    #     plt.xlabel("Shark Age Density")
    #
    #     plt.show()


plt.plot(time_steps, fish_pop, label='Fish', color='r', ls='-')
plt.plot(time_steps, shark_pop, label='Sharks', color='b', ls='-.')
plt.legend()
plt.xlabel('Time Steps')
plt.ylabel('Population (#)')
plt.title('Predator-Prey Model')
plt.show()