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
    min_x = min(x_vals)
    max_x = max(x_vals)
    min_y = min(y_vals)
    max_y = max(y_vals)

    x_offset = abs(min_x) + max_x + 1
    y_offset = abs(min_y) + max_y + 1
    offset = max(x_offset, y_offset)

    grid = [['.' for x in range(offset*2)] for y in range(offset*2)]
    for coord in coordinates:
        x = coord[0][0] + x_offset + (coord[1][0]*seconds)
        y = coord[0][1] + y_offset + (coord[1][1]*seconds)
        if x < min_x: min_x = x
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if y > max_y: max_y = y
        grid[x][y] = '#'

    # I wasn't visualizing the layout of the grid correctly
    # because the rows ended up printing out a mirror image.
    # Doing a reverse on the row fixed that. Also I was too
    # generous with my grid size, so I had to trim a lot to 
    # see it in my console (another symptom of not visualzing
    # the grid correctly). 
    for row in grid[min_x+250:max_x+10]:
        row.reverse()
        print(''.join(row[min_y+30:max_y-200]))
    
print('Solution 10.2:', seconds)


