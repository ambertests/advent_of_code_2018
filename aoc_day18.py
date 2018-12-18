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
# print_map(map)

# Observed repeating pattern after
# 475 minutes. Would be nice to find
# a way to determine this programmatically
# since this probably only works for
# my specific input
deltas = [-4069,-3506,-6435,-3051,
-345,-448,-383,3842,
1472,3026,1264,2048,
1112,6562,4698,6616,
5279,4481,1184,5672,
320,-3542,-1962,-1195,
-6809,-4332,-4070,-7429]

repeat_starts = 475
minutes = 1000000000

for i in range(repeat_starts):
    if i == 10: print('Solution 18.1:', calculate_map(map))
    map = update_map(map)

score = calculate_map(map)

remaining_minutes = minutes - repeat_starts
full_cycles = remaining_minutes / len(deltas)
remainder = remaining_minutes % len(deltas)

final_score = score + (full_cycles*sum(deltas)) + sum(deltas[:remainder])
print('Solution 18.2', int(final_score))

#print(calculate_map(map))  
      

