import os
from random import randrange
from random import choice

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
#****************************************************************************************************************

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Triangle ({self.a}, {self.b}, {self.c})'


T = Triangle(5, 10, 15)
print(T)