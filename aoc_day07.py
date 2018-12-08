
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
requirements = {}
for a in alphabet:
    requirements[a] = set()

path = []

for instruction in open('input/input07.txt').readlines():
    # Step M must be finished before step D can begin.
    split = instruction.split(' ')
    parent_letter = split[1]
    child_letter = split[7]
    requirements.get(child_letter).add(parent_letter)

def find_a_not_in_b(a, b):
    # This works by first finding what the two sets
    # have in common, than what parts of a are not in
    # that common set.
    # Example: 
    #   given a = {1,2,3}, b = {2,4,6}
    #   a.interection(b) = {2} because that is the only common value
    #   {2} ^ a = {1,3} because those are the values of a that are not {2}
    # 
    return a.intersection(b) ^ a

while len(path) < len(alphabet):
    for letter in alphabet:
        r_set = requirements[letter]
        # see if there are any requirements that aren't already in the path
        unmet = find_a_not_in_b(r_set, path)
        if not unmet and letter not in path:
            path.append(letter)
            # once we add something new to the path
            # we have to start the loop over again 
            # to maintain alphabetical order
            break

print('Solution 7.1', ''.join(path))

elves = [[] for i in range(5)]
completed = set()
in_progress = set()
total_time = 0
while len(completed) < len(path):
    for letter in path:
        if letter in completed: continue
        if letter in in_progress: continue
        work = [letter for i in range(60 + alphabet.index(letter) + 1)]
        # makes sure all requirements are complete
        unmet = find_a_not_in_b(requirements[letter], completed)
        if not unmet:
            # find a free elf and assign the work
            for elf in elves:
                if len(elf) == 0:
                    elf.extend(work)
                    in_progress.add(letter)
                    break

    # determine minimum amount of time needed to complete a step
    min_time = min([len(e) for e in elves if len(e) > 0])

    # reduce elves work by minimum time and determine completed steps
    for i in range(len(elves)):
        done = elves[i][:min_time]
        remaining = elves[i][min_time:]
        for d in set(done):
            if d not in remaining: completed.add(d)
        elves[i] = remaining
    
    total_time = total_time + min_time
    
print('Solution 7.2', total_time)


