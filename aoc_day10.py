from collections import Counter
import math
source = open('input/input10.txt').read().split('\n')

coordinates = []
for val in source:
    if not val: continue
    ## val = 'position=< 9,  1> velocity=< 0,  2>'
    position = tuple([int(i.strip()) for i in val[val.index('<')+1:val.index('>')].split(',')])
    val = val[val.index('>')+1:]
    velocity = tuple([int(i.strip()) for i in val[val.index('<')+1:val.index('>')].split(',')])
    coordinates.append((position, velocity))

has_straight_line = False
seconds = 0
min_x = 10000
max_x = 0
min_y = 10000
max_y = 0
while not has_straight_line:
    seconds += 1
    # First get all the adjusted x and y values and count them
    x_vals = [c[0][0] + c[1][0]*seconds for c in coordinates]
    y_vals = [c[0][1] + c[1][1]*seconds for c in coordinates]
    x_counter = Counter(x_vals)
    y_counter = Counter(y_vals)

    # The strategy here is to determine which version
    # of the coordinates has the greatest proportion of
    # of solid strings of x values, indicating a straight line.
    # Once the function was working, I tweaked the mxr_ratio
    # value manually, bringing the letters more into focus each time 
    mxr_ratio = 45
    mxr = Counter(x_counter.values()).most_common()[0][1]
    if math.ceil(len(coordinates)/mxr) < mxr_ratio: 
        continue
    else: 
        has_straight_line = True

    # Now that we've determined which version of the coordinates
    # is most likely to have legible letters, we can create the grid
    # according to the bounds of the adjusted coordinates
    if min(x_vals) < min_x: min_x = min(x_vals)
    if max(x_vals) > max_x: max_x = max(x_vals)
    if min(y_vals) < min_y: min_y = min(y_vals)
    if max(y_vals) > max_y: max_y = max(y_vals)

    # I was getting over-complicated here with offsets etc, thinking
    # that there would be negative point values. But by the time the 
    # letters are in focus that isn't an issue, so the regular bounding
    # values are fine  
    grid = [['.' for x in range(max_x+1)] for y in range(max_y+1)]
    for coord in coordinates:
        x = coord[0][0] + (coord[1][0]*seconds)
        y = coord[0][1] + (coord[1][1]*seconds)
        # This is the tricky bit! The way the grid prints out on the console
        # is different from how it is stored in memory. So the points need
        # to be 'rotated' by swapping the x and y values
        grid[y][x] = '#'

    # Keep the swap in place for printing and trim
    # according to the min x and y values
    for row in grid[min_y-1:]:
        print(''.join(row[min_x - 1:]))
    
print('Solution 10.2:', seconds)


