import math

def play_marbles(elf_count, turn_count):
    marbles = [0]
    scores = [0 for e in range(elf_count)]
    current_marble = 0
    total_turns = 0
    marble = 0

    while total_turns < turn_count:
        for elf in range(elf_count):
            marble += 1
            if marble % 23 != 0:
                # place the lowest-numbered remaining marble into the circle 
                # between the marbles that are 1 and 2 marbles clockwise 
                # of the current marble.
                if current_marble == len(marbles) - 1: 
                    insert_point = 1
                else: 
                    cw_1 = current_marble + 1   
                    cw_2 = current_marble + 2
                    insert_point = math.ceil((float)(cw_1 + cw_2) / 2)
                marbles.insert(insert_point, marble)
                current_marble = insert_point
            else:
                # First, the current player keeps the marble they would have placed, 
                # adding it to their score. 
                score = marble
                # In addition, the marble 7 marbles counter-clockwise from the 
                # current marble is removed from the circle and also added to the 
                # current player's score.
                if current_marble < 7: 
                    target_index = len(marbles) - (7 - current_marble) 
                else:
                    target_index = current_marble - 7

                score += marbles.pop(target_index)
                # The marble located immediately clockwise of the marble that was 
                # removed becomes the new current marble.
                current_marble = target_index
                scores[elf] += score

            total_turns += 1

    return max(scores)

# # My original solution was much much too slow to do part two.
# # At first I thought there was some mathematical solution, but it
# # comes down to using a faster algorithm. I cribbed this one from 
# # https://github.com/petertseng/adventofcode-rb-2018/blob/master/09_marble_mania.rb. 
# # 
# # It is faster because instead of using the array.insert method
# # it stretches the playing circle out into a single line which is 
# # allocated in advance. This works because really the marbles are 
# # moving back and forth on a small line segment - the circle image 
# # is not necessary to calculate each marble position.


# def play_marbles_fast(elves, marbles):
#     clockwise = [None for m in range(marbles + 1)]
#     clockwise[0] = 0
#     scores = [0 for e in range(elves)]
#     current = 0
#     for marble in range(1,marbles + 1):
#         if marble % 23 != 0:
#             clockwise[marble] = clockwise[clockwise[current]]
#             clockwise[clockwise[current]] = marble
#             current = marble
#         else:
#             removed = clockwise[marble - 5]
#             scores[marble % elves] += marble + removed
#             # This line is black magic - how does it work??
#             current = clockwise[marble - 5] = clockwise[removed]
#     return max(scores)

# This linked list solution is not as fast as the one above, but
# I can actually understand what it is doing instead of feeling 
# like the solution is black magic.
class Marble:
    value = 0
    prev = None
    next = None
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

def play_marbles_ll(elves,  marbles):
    marble_zero = Marble(0, None, None)
    marble_zero.prev = marble_zero
    marble_zero.next = marble_zero
    current = marble_zero
    scores = [0 for e in range(elves)]
    for marble in range(1, marbles+1):
        if marble % 23 != 0:
            cw_1 = current.next
            cw_2 = current.next.next
            new_marble = Marble(marble, cw_1, cw_2)
            cw_2.prev = new_marble
            cw_1.next = new_marble
            current = new_marble
        else:
            player = (marble % elves)
            scores[player] += marble
            current = current.prev.prev.prev.prev.prev.prev.prev
            scores[player] += current.value
            current.prev.next = current.next
            current.next.prev = current.prev
            current = current.next
    return max(scores)

# ** 10 players; last marble is worth 1618 points: high score is 8317
# 13 players; last marble is worth 7999 points: high score is 146373
# ** 17 players; last marble is worth 1104 points: high score is 2764
# ** 21 players; last marble is worth 6111 points: high score is 54718
# ** 30 players; last marble is worth 5807 points: high score is 37305

print(9, 25, play_marbles_ll(9, 25))
print(10, 1618, play_marbles_ll(10, 1618))
# My original solution didn't get this example right,
# but the fast algorithm did - why???? Something to
# do with calculating the new index at the top
# of the circle...
print('***',13, 7999, play_marbles(13, 7999))
print(13, 7999, play_marbles_ll(13, 7999))
print(17, 1104, play_marbles_ll(17, 1104))
print(21, 6111, play_marbles_ll(21, 6111))
print(30, 5807, play_marbles_ll(30, 5807))


# # 432 players; last marble is worth 71019 points        
print('Solution 9.1:', play_marbles_ll(432, 71019))

# # What would the new winning Elf's score be 
# # if the number of the last marble were 100 times larger?


# # The original method is super slow....
print('Solution 9.2:', play_marbles_ll(432, 7101900))