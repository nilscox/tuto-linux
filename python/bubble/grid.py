import events
from calculations import grid_cells, grid_cell_position
from cell import Cell


class Grid:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cells = []
        self.bubble = None

        events.subscribe('fire', self.on_fire)

        for i in range(grid_cells()):
            cell = Cell(self.canvas, grid_cell_position(i))
            self.cells.append(cell)

    def on_fire(self, bubble):
        self.bubble = bubble

    def update(self):
        if self.bubble is not None:
            self.bubble.update()
            for cell in self.cells:
                cell.check_collisions(self.bubble)
