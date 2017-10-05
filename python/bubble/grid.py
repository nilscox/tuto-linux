from calculations import grid_cells, grid_cell_position
from cell import Cell


class Grid:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cells = []

        for i in range(grid_cells()):
            cell = Cell(self.canvas, grid_cell_position(i))
            self.cells.append(cell)
            print(cell.position)

    def update(self, bubble):
        for cell in self.cells:
            cell.check_collisions(bubble)
