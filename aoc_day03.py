import requests, sys

# Grab the session cookie from the https://adventofcode.com/2018 site:
# right-click, Inspect, Application tab, Cookies, session.
# Call from command line with "python3 aoc_day01.py <session>"
session = sys.argv[1]

url = "https://adventofcode.com/2018/day/3/input"
headers = {
	'cookie': "session=" + session
	}

input = requests.request("GET", url, headers=headers)
# cut off the last value because it is an empty string
coord_list = input.text.split('\n')[:-1]

# Part One:

fabric = [[0 for y in range(1000)] for x in range(1000)]
overlap = 0
for coord in coord_list:
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
                # mark overlap with a -1 so it is only counted once
                if fabric[x][y] > 0:
                    fabric[x][y] = -1
                    overlap = overlap + 1

print('Solution 3.1: ', overlap)

for coord in coord_list:
    # yes, it is lazy to copy/paste the string splitting...
    id = int(coord[1:coord.index(' @ ')])
    x_offset = int(coord[coord.index(' @ ') + 3:coord.index(',')])
    y_offset = int(coord[coord.index(',')+1:coord.index(':')])
    width = int(coord[coord.index(': ')+2:coord.index('x')])
    height = int(coord[coord.index('x')+1:])
    overlapped = False
    for x in [i+x_offset for i in range(width)]:
        for y in [j+y_offset for j in range(height)]:
            if fabric[x][y] == -1:
                overlapped = True
                break
        if overlapped: break
    if not overlapped: print('Solution 3.2: ', id)


