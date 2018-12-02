import requests, sys

# Grab the session cookie from the https://adventofcode.com/2018 site:
# right-click, Inspect, Application tab, Cookies, session.
# Call from command line with "python3 aoc_day01.py <session>"
session = sys.argv[1]

url = "https://adventofcode.com/2018/day/2/input"
headers = {
	'cookie': "session=" + session
	}

input = requests.request("GET", url, headers=headers)
# cut off the last value because it is an empty string
id_list = input.text.split('\n')[:-1]

# Part One:
# To make sure you didn't miss any, you scan the likely candidate boxes again, 
# counting the number that have an ID containing exactly two of any letter 
# and then separately counting those with exactly three of any letter. 
# You can multiply those two counts together to get a rudimentary checksum 
# and compare it to what your device predicts.

two_count = 0
three_count = 0
for id in id_list:
    letter_counts = {}
    has_two = False
    has_three = False
    for i in range(len(id)):
        ch = id[i]
        if ch in letter_counts:
            letter_counts[ch] = letter_counts[ch] + 1
        else:
            letter_counts[ch] = 1
    for letter in letter_counts:
        if not has_two and letter_counts[letter] == 2:
            two_count = two_count + 1
            has_two = True
        if not has_three and letter_counts[letter] == 3:
            three_count = three_count + 1
            has_three = True


print('Solution 2.1: ', two_count * three_count)

# Part 2
# The boxes will have IDs which differ by exactly 
# one character at the same position in both strings. 
# For example, given the following box IDs:

# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz

# The IDs abcde and axcye are close, but they differ by 
# two characters (the second and fourth).However, the 
# IDs fghij and fguij differ by exactly one character, 
# the third (h and u). Those must be the correct boxes.

# What letters are common between the two correct box IDs? 
# (In the example above, this is found by removing the 
# differing character from either ID, producing fgij.)

diff_count = 0
common = ''
# Very brute force, but it works reasonably quickly
for a in range(0, len(id_list) - 1):
    id_a = id_list[a]
    for b in range(1, len(id_list)):
        id_b = id_list[b]
        for i in range(len(id_a)):
            if id_a[i] != id_b[i]:
                diff_count = diff_count + 1
                if diff_count > 1:
                    break
            else:
                common = common + id_a[i]
        if diff_count == 1:
            print('Solution 2.2: ',common)
            break
        else:
            diff_count = 0
            common = ''

    if diff_count == 1:
        break



			

