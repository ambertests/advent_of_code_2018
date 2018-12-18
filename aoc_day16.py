
def addr(i, r): 
    r[i[3]] = r[i[1]] + r[i[2]]
    return r

def addi(i, r): 
    r[i[3]] = r[i[1]] + i[2]
    return r

def mulr(i, r): 
    r[i[3]] = r[i[1]] * r[i[2]]
    return r

def muli(i, r): 
    r[i[3]] = r[i[1]] * i[2]
    return r

def banr(i, r): 
    r[i[3]] = r[i[1]] & r[i[2]]
    return r

def bani(i, r): 
    r[i[3]] = r[i[1]] & i[2]
    return r

def borr(i, r): 
    r[i[3]] = r[i[1]] | r[i[2]]
    return r

def bori(i, r): 
    r[i[3]] = r[i[1]] | i[2]
    return r

def setr(i, r): 
    r[i[3]] = r[i[1]]
    return r
    
def seti(i, r): 
    r[i[3]] = i[1]
    return r

def gtir(i, r): 
    r[i[3]] = int(i[1] > r[i[2]])
    return r

def gtri(i, r): 
    r[i[3]] = int(r[i[1]] > i[2])
    return r

def gtrr(i, r): 
    r[i[3]] = int(r[i[1]] > r[i[2]])
    return r

def eqir(i, r): 
    r[i[3]] = int(i[1] == r[i[2]])
    return r

def eqri(i, r): 
    r[i[3]] = int(r[i[1]] == i[2])
    return r

def eqrr(i, r): 
    r[i[3]] = int(r[i[1]] == r[i[2]])
    return r

opcodes = [ 'addr','addi','mulr','muli',
            'banr','bani','borr','bori',
            'setr','seti','gtir','gtri',
            'gtrr','eqir','eqri','eqrr']

def parse(logs):
    parsed = []
    did_after = False
    for log in logs.split('\n'):
        if len(log):
            if log.startswith('Before'):
                before = eval(log.split(': ')[1])
            elif log.startswith('After'):
                after = eval(log.split(': ')[1])
                did_after = True
            else: inst = [int(x) for x in log.split(' ')]
        if did_after: 
            parsed.append((before, inst, after))
            did_after = False
    return parsed


test = '''Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]'''

samples = parse(open('input/input16_1.txt').read())

has_three = 0
for o in samples:
    valid = 0
    for op in opcodes:
        eval_str = '%s(%s,%s)' % (op, o[1], o[0])
        if eval(eval_str) == o[2]: valid += 1
    if valid >= 3: 
        has_three += 1

print('Solution 16.1:', has_three)

codes = [None for i in range(16)]
while None in codes:
    for s in samples:
        valid = []
        for op in opcodes:
            opnum = s[1][0]
            # only check the codes that haven't been validated
            if op not in codes:
                eval_str = '%s(%s,%s)' % (op, s[1], s[0])
                if eval(eval_str) == s[2]: 
                    valid.append((opnum,op))
        # if there is only one valid solution 
        # assign the code to that number
        if len(valid) == 1: 
            codes[valid[0][0]] = valid[0][1]

program = open('input/input16_2.txt').read().split('\n')
register = [0,0,0,0]
for line in program:
    inst = inst = [int(x) for x in line.split(' ')]
    eval_str = '%s(%s,%s)' % (codes[inst[0]], inst, register)
    register = eval(eval_str)

print('Solution 16.2:', register[0])


