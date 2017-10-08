import events
from calculations import grid_cells, grid_cell_position, grid_bubble_collision
from cell import Cell


class Grid:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cells = []
        self.bubble = None

        events.subscribe('fire', self.on_fire)
        events.subscribe('attach', self.on_attach)

        for i in range(grid_cells()):
            cell = Cell(self.canvas, grid_cell_position(i), i)
            self.cells.append(cell)

    def on_fire(self, bubble):
        self.bubble = bubble

    def on_attach(self):
        self.bubble = None

    def update(self):
        if self.bubble is not None:
            self.bubble.update()
            grid_bubble_collision(self.cells, self.bubble)
