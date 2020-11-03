#print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
#print("A| ◼ | ◼ | ◼ | ◼ | ◼ | ◼ |")
#print("B| □ | □ | □ | □ | □ | □ |")
#print("C| □ | ✖ | □ | □ | □ | □ |")
#print("D| □ | □ | □ | □ | □ | □ |")
#print("E| □ | □ | □ | □ | □ | □ |")
#print("F| □ | □ | □ | □ | □ | □ |")
#print("G| ✖ | □ | □ | □ | □ | ● |")

# ■ □ ✖ ●

class FieldPart(object):
    main = 'map'
    radar = 'radar'
    weight = 'weight'

class Color:
    white = '\033[0;37m'
    reset = '\033[0m'
    blue = '\033[0;34m'
    yellow = '\033[0;33m'
    red = '\033[0;31m'
    miss = '\033[0;37m'

def set_color(text, color):
    return color + text + Color.reset

class Cell(object):
    empty_cell = set_color('□', Color.white)
    ship_cell = set_color('■', Color.blue)
    destroyed_ship = set_color('✖', Color.red)
    damaged_ship = set_color('●', Color.yellow)
    miss_cell = set_color('☉', Color.miss)

class Field(object):

    def __init__(self, size):
        self.size = size
        self.map = [[Cell.empty_cell for _ in range(size)] for _ in range(size)]
        self.radar = [[Cell.empty_cell for _ in range(size)] for _ in range(size)]
        self.weight = [[1 for _ in range(size)] for _ in range(size)]

