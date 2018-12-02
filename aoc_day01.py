import requests, sys

# Grab the session cookie from the https://adventofcode.com/2018 site:
# right-click, Inspect, Application tab, Cookies, session.
# Call from command line with "python3 aoc_day01.py <session>"
session = sys.argv[1]

url = "https://adventofcode.com/2018/day/1/input"
headers = {
	'cookie': "session=" + session
	}

input = requests.request("GET", url, headers=headers)

# Part One:
# Starting with a frequency of zero, what is the resulting frequency 
# after all of the changes in frequency have been applied?

# cut off the last value because it is an empty string
int_list = [int(x) for x in input.text.split('\n')[:-1]]
print('Solution 1.1: ', sum(int_list))

# Part Two:
# You notice that the device repeats the same frequency change list over and over. 
# To calibrate the device, you need to find the first frequency it reaches twice.

# My initial solution used a list but a set is a bazillion times faster
uniq_dest = set([0])
dest = 0
found_repeat = False
index = 0
max_index = len(int_list) - 1
while not found_repeat:
	dest = dest + int_list[index]
	if dest in uniq_dest:
		print('Solution 1.2: ', dest)
		found_repeat = True
		break
	else:
		uniq_dest.add(dest)
		if index < max_index: index = index + 1
		else: index = 0
			

