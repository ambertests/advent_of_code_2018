input = open('input/input12.txt').readlines()
plants = []
ZERO = 5
BASE_GEN_COUNT = 0
FINAL_GEN_COUNT = 50000000000
will_grow = set()
wont_grow = set()
for line in input:
    line = line.strip()
    if line.startswith('initial'):
        pots = list(line.split(' ')[2])
        BASE_GEN_COUNT = len(pots)
        plants = ['.' for p in range(len(pots) + BASE_GEN_COUNT + ZERO)]
        for pot in range(len(pots)):
            plants[ZERO + pot] = pots[pot]

    elif line.endswith('#'):
        will_grow.add(line.split(' => ')[0])
    elif line.endswith('.'):
        wont_grow.add(line.split(' => ')[0])

def get_plant_total():
    total = 0
    for i in range(len(plants)):
        if plants[i] == '#': total += (i - ZERO)
    return total

# I observed through experimentation that the change delta stayed the
# same after the 100th generation, so it is only necessary to calculate
# up to there. I'm guessing it is 100 because that is the length of the 
# initial string. Surely there is an official name for this statistical
# pattern, but I don't know what it is...
plant_count = get_plant_total()
last_delta = 0
for g in range(BASE_GEN_COUNT):
    if g == 20: print('Solution 12.1:', plant_count)
    new_gen = ['.' for i in range(len(plants))]
    for p in range(len(plants) - 5):
        segment = ''.join(plants[p:p+5])
        if segment in will_grow:
            new_gen[p+2] = '#'
        elif segment in wont_grow:
            new_gen[p+2] = '.'
    plants = new_gen
    new_plant_count = get_plant_total()
    new_delta = new_plant_count - plant_count
    if last_delta != new_delta:
        # print(g, 'to', g+1, 'delta from', last_delta, 'to', new_delta)
        last_delta = new_delta
    plant_count = new_plant_count

print('Solution 12.2:', plant_count + ((FINAL_GEN_COUNT - BASE_GEN_COUNT)*last_delta))
