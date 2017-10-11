from time import time

import events
from constants import GRID_LINE_SPAWN_TIME
from cursor import Cursor
from grid import Grid
from panel import Panel


class Game:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cursor = Cursor(canvas)
        self.grid = Grid(canvas)
        self.last_line_spawn = time()
        self.lost = False

    def has_lost(self):
        for cell in self.grid.get_last_line():
            if cell.has_bubble():
                return True

        return False

    def update(self, ellapsed):
        if self.lost:
            return

        now = time()
        diff = now - self.last_line_spawn

        if diff >= GRID_LINE_SPAWN_TIME:
            self.grid.spawn_line()
            self.grid.detach_isolated_bubbles()
            self.last_line_spawn = now

        self.grid.update(ellapsed)

        for bubble in self.grid.get_falling_bubbles():
            bubble.update(ellapsed)

        if self.has_lost():
            self.lost = True
            Panel(self.canvas, 'You have lost the game.')
            events.publish('lost')
