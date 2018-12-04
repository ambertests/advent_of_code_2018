
# Part One:
# Starting with a frequency of zero, what is the resulting frequency 
# after all of the changes in frequency have been applied?

input = open('input/input01.txt').readlines()
int_list = [int(x.strip()) for x in input]
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
			

