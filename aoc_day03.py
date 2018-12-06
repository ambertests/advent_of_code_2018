
input = [x.strip() for x in open('input/input03.txt').readlines()]

# Part One:

fabric = [[0 for y in range(1000)] for x in range(1000)]
overlap = 0
no_overlap_ids = []
for coord in input:
    has_overlap = False
    # #35 @ 923,270: 12x22
    id = int(coord[1:coord.index(' @ ')])
    x_offset = int(coord[coord.index(' @ ') + 3:coord.index(',')])
    y_offset = int(coord[coord.index(',')+1:coord.index(':')])
    width = int(coord[coord.index(': ')+2:coord.index('x')])
    height = int(coord[coord.index('x')+1:])
    for x in [i+x_offset for i in range(width)]:
        for y in [j+y_offset for j in range(height)]:
            if fabric[x][y] == 0: fabric[x][y] = id
            else:
                has_overlap = True
                if fabric[x][y] > 0:
                    if fabric[x][y] in no_overlap_ids: 
                        no_overlap_ids.remove(fabric[x][y])
                    # mark overlap with a -1 so it is only counted once
                    fabric[x][y] = -1
                    overlap = overlap + 1
    if not has_overlap: no_overlap_ids.append(id)

print('Solution 3.1:', overlap)
print('Solution 3.2:', no_overlap_ids)



