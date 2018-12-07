
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
requirements = {}
for a in alphabet:
    requirements[a] = set()

path = []

for instruction in open('input/input07.txt').readlines():
    # Step M must be finished before step D can begin.
    parent_letter = instruction[5:6]
    child_letter = instruction[36:37]
    requirements.get(child_letter).add(parent_letter)

while len(path) < len(alphabet):
    for letter in alphabet:
        r_set = requirements[letter]
        # see if there are any requirements that aren't already in the path
        required = r_set.intersection(set(path)) ^ r_set
        if len(required) == 0 and letter not in path:
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
    for p in path:
        if p in completed: continue
        if p in in_progress: continue
        work = [p for i in range(60 + alphabet.index(p) + 1)]
        # makes sure all requirements are complete
        r_set = requirements[p]
        required = r_set.intersection(set(completed)) ^ r_set
        if not required:
            # find a free elf and assign the work
            for elf in elves:
                if len(elf) == 0:
                    elf.extend(work)
                    in_progress.add(p)
                    break

    # determine minimum amount of time needed to complete a step
    min_time = 100000
    for e in elves:
        if e and len(e) < min_time: min_time = len(e)

    # reduce elves work by minimum time and determine completed steps
    for i in range(len(elves)):
        done = elves[i][:min_time]
        remaining = elves[i][min_time:]
        for d in set(done):
            if d not in remaining: completed.add(d)
        elves[i] = remaining
    
    total_time = total_time + min_time
    
print('Solution 7.2', total_time)

