
coordinates = []
min_x = 1000
max_x = 0
min_y = 1000
max_y = 0
for l in open('input/input06.txt').readlines():
    coord = l.split(', ')
    x = int(coord[0].strip())
    y = int(coord[1].strip())
    if x < min_x: min_x = x
    if x > max_x: max_x = x
    if y < min_y: min_y = y
    if y > max_y: max_y = y
    
    coordinates.append((x,y))


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_edge(pt):
    return pt[0] == min_x or pt[0] == max_x or pt[1] == min_y or pt[1] == max_y

# point_index matched with set of closest points (Part 1)
point_counts = {}

# list of points which reach all coordinates within 10000 total distance (Part 2)
part2_points = []


# This one gave me so much trouble!! I had the correct strategy early on,
# but missed that the range needed to *inclue* the max x and y, so I
# wasted a lot of time with over-complex checks of other things
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        current_point = (x,y)
        min_distance = 1000000
        closest = None
        distances = []
        for coord in coordinates:
            distance = manhattan_distance(coord, current_point)
            distances.append(distance)
            if distance < min_distance:
                min_distance = distance
                closest = coord
            # if the point is equidistant to multiple coordinates
            # then it doesn't count to overall area of the one coordinate
            elif distance == min_distance:
                closest = None
        if closest:
            # areas on the edge are infinite, so don't count in area calculation
            if is_edge(current_point): point_counts[closest] = -1
            else:
                point_counts[closest] = point_counts.get(closest, 0) + 1

        if sum(distances) < 10000: part2_points.append(current_point)



print('Solution 6.1:', max(point_counts.values()))
print('Solution 6.2:', len(part2_points))

            
            
            