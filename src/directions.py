import curses
from enum import Enum

class Directions(Enum):
    RIGHT = curses.KEY_RIGHT
    LEFT = curses.KEY_LEFT
    UP = curses.KEY_UP
    DOWN = curses.KEY_DOWN
