
def reduce_polymer(orig, to_remove=None, max_len=-1):
    polymer = []
    for i in range(len(orig)):
        # We save a lot of processing time for Part 2
        # if we cut off the string building once the 
        # array is too long
        if max_len > 0 and len(polymer) >= max_len: return None

        # The test character for Part 2 is 'removed'
        # by just not adding it to the polymer array
        if to_remove and orig[i].lower() == to_remove: continue
        
        polymer.append(orig[i])
        end_pair = polymer[len(polymer)-2:]
        while len(polymer) > 1 and end_pair[0] != end_pair[1] and end_pair[0].lower() == end_pair[1].lower():
            # If the end pair meets the criteria of being a matched upper and lower case
            # then remove it from the end of the array. Repeat until the end pair is not removed
            polymer = polymer[:-2]
            end_pair = polymer[len(polymer)-2:]
    return polymer
    
    
input = open('input/input05.txt').read()
print('Solution 5.1:', len(reduce_polymer(input)))

distinct_char = set(input.lower())
min_len = len(input)
char_to_remove = ''

for c in distinct_char:
    poly = reduce_polymer(input, c, min_len)
    if poly is not None and len(poly) < min_len:
        min_len = len(poly)
        char_to_remove = c
        
print('Most troublesome character is', char_to_remove)
print('Solution 5.2:', min_len)

    

