
import numpy as np
from collections import defaultdict, namedtuple
from time import time
SERIAL_NUMBER = 6548

def get_power_level(x, y, sn):
    rack_id = x + 10
    power = y * rack_id
    power += sn
    power *= rack_id
    hd = int(str(power)[:-2][-1:])
    return hd - 5

# Fuel cell at  122,79, grid serial number 57: power level -5.
# Fuel cell at 217,196, grid serial number 39: power level  0.
# Fuel cell at 101,153, grid serial number 71: power level  4.

assert(get_power_level(122,79,57) == -5)
assert(get_power_level(217,196,39) == 0)
assert(get_power_level(101,153,71) == 4)


# I was able to do Part 1 on my own grinding through a list
# of lists to represent the power grid. However, for Part 2 that
# basic strategy was way too slow - I didn't have the patience
# to let it finish, plus I had to go to work...
def solve_day_11_slow(run_part_2=False):
    start = time()
    max_power = 0
    max_power_point = (0,0)
    grid = [[0 for x in range(300)] for y in range(300)]
    for x in range(300):
        for y in range(300):
            grid[x][y] = get_power_level(x+1, y+1, SERIAL_NUMBER)
    
    for x in range(298):
        for y in range(298):
            power = 0
            for i in range(3):
                for j in range(3):
                    power += grid[x+i][y+j]
            if power > max_power:
                max_power = power
                max_power_point = (x,y)
    print("Solution 11.1:", max_power_point[0]+1, max_power_point[1]+1)
    print("Running time:", time() - start)
    if run_part_2:
        start = time()
        max_power = 0
        max_power_point = (0,0)
        max_size = 0
        for size in range(1,301):
            print("Checking size:", size)
            # if max_power == 121: break
            # This is a hack to narrow the search box
            # around the current max point - it worked
            # for my serial number but can't guarantee
            x_start = max(0, max_power_point[0] - 30)
            for x in range(x_start, 301 - size):
                y_start = max(0, max_power_point[1] - 30)
                for y in range(y_start, 301 - size):
                    power = 0
                    for i in range(size):
                        for j in range(size):
                            power += grid[x+i][y+j]
                    if power > max_power:
                        print("New max:", power, "at", (x+1,y+1), size)
                        max_power = power
                        max_power_point = (x,y)
                        max_size = size
        print("Solution 11.2:", max_power_point[0]+1, max_power_point[1]+1, max_size)
        print("Running time:", time() - start)

# I ended up cribbing this solution from
# https://github.com/stacybrock/advent-of-code/blob/master/2018/11/power.py
# It is the same basic idea, but speeded up considerably by using
# defaultdict and numpy to help with the gruntwork. 
def solve_day_11_medium():
    start = time()
    grid = np.zeros((300,300))
    for (x_,y_), power in np.ndenumerate(grid):
        grid[y_][x_] = get_power_level(x_+1, y_+1, SERIAL_NUMBER)

    threes = defaultdict(int)
    for y in range(0, 298):
        for x in range(0, 298):
            threes[(x+1,y+1)] = np.sum(grid[y:y+3, x:x+3])
    print('Solution 11.1:', max(threes, key=threes.get))
    print("Running time:", time() - start)
    start = time()

    squares = defaultdict(int)
    for size in range(1, 301):
        max_power = 0
        Power = namedtuple('Power', 'x y size power')
        for y in range(0, 301-size):
            for x in range(0, 301-size):
                power = np.sum(grid[y:y+size, x:x+size])
                if power > max_power:
                    running = Power(x,y,size,power)
                    max_power = power
        squares[(running.x+1, running.y+1, running.size)] = running.power
    print('Solution 11.2:', max(squares, key=squares.get))
    print("Running time:", time() - start)

# This solution from
# https://github.com/badouralix/advent-of-code-2018/blob/master/day-11/part-2/silvestre.py
# is almost instant, but when I look at the code, 
# I don't understand what it is doing, so...
def solve_day_11_part_2_fast():
    start = time()
    rack_id = np.arange(1, 301).reshape(-1, 1) + 10
    grid = rack_id * np.arange(1, 301).reshape(1, -1) # broadcasting
    grid += SERIAL_NUMBER
    grid *= rack_id
    grid %= 1000
    grid //= 100
    grid -= 5

    X = np.zeros((301, 301))
    X[1:, 1:] = grid.cumsum(axis=0).cumsum(axis=1)

    maximum = 0
    ret = (None, None, None)
    for size in range(1, 301):
        tmp = X[size:, size:] + X[:-size, :-size] - X[size:, :-size] - X[:-size, size:]
        if tmp.max() > maximum:
            maximum = tmp.max()
            x, y = np.unravel_index(tmp.argmax(), tmp.shape)
            ret = (x+1, y+1, size)

    print("Solution 11.2:", "{},{},{}".format(*ret))
    print("Running time:", time() - start)


print("Run my original solution")
# Set to True to run the attempted Part 2 solution
# I never had the patience to let it run all the way
# although in retrospect it got to the correct answer
# within 20 seconds
solve_day_11_slow(True)
print("\nRun better solution from stacybrock")
solve_day_11_medium()
print("\nRun amazing super fast solution from badouralix")
solve_day_11_part_2_fast()