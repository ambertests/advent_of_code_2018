test = '''.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.'''


def parse(input_str):
    lines = input_str.split('\n')
    map = [['' for i in range(len(lines[0]))]for j in range(len(lines))]
    for y in range(len(lines)):
        row = lines[y]
        for x in range(len(row)):
            map[y][x] = row[x]
    return map


def update_map(map):
    max_y = len(map)
    max_x = len(map[0])
    new_map = [['.' for y in range(max_y)] for x in range(max_x)]
    for y in range(max_y):
        for x in range(max_x):
            trees = []
            yards = []
            opn = []
            adj = [
                (x-1, y-1), (x, y-1), (x+1, y-1),
                (x-1, y),             (x+1, y),
                (x-1, y+1), (x, y+1), (x+1, y+1)
                ]
            for a in adj:
                if a[0] < 0 or a[0] >= max_x or a[1] < 0 or a[1] >= max_y: continue
                ch = map[a[1]][a[0]]
                if ch == '#': yards.append(a)
                elif ch == '|': trees.append(a)
                else: opn.append(a)
            t = map[y][x]
            new_char = t
            if t == '.' and len(trees) >= 3: new_char = '|'
            elif t == '|' and len(yards) >= 3: new_char = '#'
            elif t == '#' and (len(yards) == 0 or len(trees) == 0): new_char = '.'
            new_map[y][x] = new_char
    
    return new_map

def print_map(map):               
    for row in map:
        print(''.join(row))
    print('\n')

def calculate_map(map):
    tree_count = 0
    yard_count = 0
    for row in map:
        for c in row:
            if c == '|': tree_count += 1
            elif c == '#': yard_count += 1
    return tree_count * yard_count

map = parse(open("input/input18.txt").read())
total_minutes = 1000000000

deltas = set()
repeated = []
minute = 0
score = 0
streak = 0
while minute < total_minutes:
    map = update_map(map)
    new_score = calculate_map(map)
    if minute == 9: print('Solution 18.1:', calculate_map(map))
    delta = new_score - score
    if delta in deltas:
        # once the repeat streak is equal to the length
        # of repeated deltas, the pattern is established
        if delta in repeated and streak % len(repeated) == 0:
            break
        else: 
            streak += 1
            repeated.append(delta)
    else:
        streak = 0
        repeated.clear()
        deltas.add(delta)
    score = new_score
    minute += 1

remaining_minutes = total_minutes - minute

# number of times to apply the full set of deltas
full_cycles = remaining_minutes / len(repeated) 

# number of leftover deltas to apply at the end
remainder = remaining_minutes % len(repeated) 

final_score = score + (full_cycles*sum(repeated)) + sum(repeated[:remainder])
print('Solution 18.2', int(final_score))

      

