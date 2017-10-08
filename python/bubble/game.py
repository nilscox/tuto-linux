from calculations import cell_position
from cursor import Cursor
from grid import Grid


class Game:

    def __init__(self, canvas):
        self.cursor = Cursor(canvas)
        self.grid = Grid(canvas)

        for c in self.grid.cells[22].get_adjacent(self.grid.cells):
            c.square = canvas.create_rectangle(*cell_position(c.position), fill='blue')

    def update(self):
        self.grid.update()
