

board = [3,7]
elf1 = 0
elf2 = 1

input = 110201

def add_recipes():
    global elf1, elf2
    score = board[elf1] + board[elf2]
    if score < 10: board.append(score)
    else:
        board.append(1)
        board.append(score%10)
    elf1 = (elf1 + board[elf1] + 1) % len(board)
    elf2 = (elf2 + board[elf2] + 1) % len(board)


while len(board) < input + 10:
    add_recipes()
print('Solution 14.1:', ''.join([str(x) for x in board[-10:]]))


board = [3,7]
elf1 = 0
elf2 = 1
found = False
target = [int(x) for x in str(input)]
while not found:
    add_recipes()
    if len(board) < len(target): continue
    if board[-len(target):] == target:
        found = True
        print('Solution 14.2:', len(board) - len(target))
        break
    # need to also do an offset check because it could have been two added
    if board[-len(target) - 1:-1] == target:
        found = True
        print('Solution 14.2:', len(board) - len(target) - 1)
        break




    

        
