
slashes = set()
back_slashes = set()
horizontals = set()
verticals = set()
pluses = set()

LEFT = '<'
RIGHT = '>'
UP = '^'
DOWN = 'v'

TURN_SEQUENCE = ['L', 'S', 'R']

carts = []

class Cart():

    def __init__(self, point, orientation, id):
        self.orientation = orientation
        self.point = point
        self.turn_count = 0
        self.crashed = False
        self.id = id

    def _next_point(self):
        point = self.point
        if self.orientation == LEFT:
            point = (point[0]-1, point[1]) 
        elif self.orientation == RIGHT:
            point = (point[0]+1, point[1]) 
        elif self.orientation == UP:
            point = (point[0], point[1]-1) 
        elif self.orientation == DOWN:
            point = (point[0], point[1]+1) 
        self.point = point

    def __repr__(self):
        return '[%s, %s]' % (str(self.point), self.orientation)

    def _turn_right(self):
        if self.orientation == LEFT: self.orientation = UP 
        elif self.orientation == RIGHT: self.orientation = DOWN
        elif self.orientation == UP: self.orientation = RIGHT
        elif self.orientation == DOWN: self.orientation = LEFT

    def _turn_left(self):
        if self.orientation == LEFT: self.orientation = DOWN
        elif self.orientation == RIGHT: self.orientation = UP
        elif self.orientation == UP: self.orientation = LEFT
        elif self.orientation == DOWN: self.orientation = RIGHT


    def _turn_corner(self):
        if self.point in slashes:
            if self.orientation in [UP, DOWN]: self._turn_right()
            else: self._turn_left()
        elif self.point in back_slashes:
            if self.orientation in [UP, DOWN]: self._turn_left()
            else: self._turn_right()
    
    def _intersection(self):
        turn_type = TURN_SEQUENCE[self.turn_count % len(TURN_SEQUENCE)]
        if self.point in pluses:
            if turn_type == 'L': self._turn_left()
            elif turn_type == 'R': self._turn_right()
            self.turn_count += 1


    def move_next(self):
        self._next_point()
        self._turn_corner()
        self._intersection()
        return self.point

def clear_all():
    carts.clear()
    slashes.clear()
    pluses.clear()
    back_slashes.clear()
    horizontals.clear()
    verticals.clear()

def fill_map(input):
    cart_num = 1
    clear_all()
    map = [list(line) for line in input.split('\n')]
    for y in range(len(map)):
        for x in range(len(map[y])):
            char = map[y][x]
            if char == ' ': continue
            point = (x,y)
            if char == '/': slashes.add(point)
            elif char == '\\': back_slashes.add(point)
            elif char == '-': horizontals.add(point)
            elif char == '|': verticals.add(point)
            elif char == '+': pluses.add(point)
            else: # it's a cart
                carts.append(Cart(point, char, cart_num))
                cart_num += 1
    return map

def print_map(map):
    for y in range(len(map)):
        p_row = map[y].copy()
        for x in range(len(p_row)):
            has_cart = False
            for cart in carts:
                if (x, y)  == cart.point:
                    if has_cart:
                        p_row[x] = 'X'
                    else:
                        p_row[x] = cart.orientation
                        has_cart = True
            if not has_cart:
                if p_row[x] in [LEFT, RIGHT]: p_row[x] = '-'
                if p_row[x] in [UP, DOWN]: p_row[x] = '|'
        print(''.join(p_row))
    print('')

input = open('input/input13.txt').read()

part_1_test_input = '''/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/  '''

part_2_test_input = '''/>-<\\  
|   |  
| /<+-\\
| | | v
\\>+</ |
  |   ^
  \\<->/'''


map = fill_map(input)
ticks = 0
crashed = 0
while len(carts) - crashed > 1:
    ticks += 1
    for cart in carts:
        if cart.crashed: continue
        points = set([c.point for c in carts if not c.crashed])
        p = cart.move_next() 
        if p in points:
            for c in carts:
                if c.point[0] == p[0] and c.point[1] == p[1] and c.id != cart.id :
                    c.crashed = True

            # print('Collison', p, ticks)
            cart.crashed = True
            if crashed == 0: print('Solition 13.1:', p)

    crashed = len([c for c in carts if c.crashed])
    carts = sorted(carts, key = lambda cart: (cart.point[1], cart.point[0]))

print('Solution 13.2', [cart for cart in carts if not cart.crashed][0].point)



