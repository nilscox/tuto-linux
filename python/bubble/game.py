from cursor import Cursor
from grid import Grid


class Game:

    def __init__(self, canvas):
        self.cursor = Cursor(canvas)
        self.grid = Grid(canvas)

    def update(self):
        self.grid.update()
