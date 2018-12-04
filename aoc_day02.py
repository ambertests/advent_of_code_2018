
input = [x.strip() for x in open('input/input02.txt').readlines()]

# Part One:
# To make sure you didn't miss any, you scan the likely candidate boxes again, 
# counting the number that have an ID containing exactly two of any letter 
# and then separately counting those with exactly three of any letter. 
# You can multiply those two counts together to get a rudimentary checksum 
# and compare it to what your device predicts.

# Initial solution was doing the character count by hand
# but why roll my own when Python has a Counter object?
from collections import Counter

two_count = 0
three_count = 0
for id in input:
    counter = Counter(id)
    if 2 in counter.values(): two_count = two_count + 1
    if 3 in counter.values(): three_count = three_count + 1

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
for a in range(0, len(input) - 1):
    id_a = input[a]
    # start the inner loop at the next after a
    # because we don't need to look at the ones behind
    for b in range(a+1, len(input)):
        id_b = input[b]
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



			

