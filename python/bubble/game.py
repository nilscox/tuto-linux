from time import time

from constants import GRID_LINE_SPAWN_TIME
from cursor import Cursor
from grid import Grid


class Game:

    def __init__(self, canvas):
        self.cursor = Cursor(canvas)
        self.grid = Grid(canvas)
        self.last_line_spawn = time()
    def update(self, ellapsed):

        now = time()
        diff = now - self.last_line_spawn

        if diff >= GRID_LINE_SPAWN_TIME:
            self.grid.spawn_line()
            self.last_line_spawn = now

        self.grid.update(ellapsed)
