import events
from constants import GRID_LINES, GRID_COLS
from calculations import grid_collision
from cell import Cell


class Grid:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cells = []
        self.bubble = None

        events.subscribe('fire', self.on_fire)
        events.subscribe('attach', self.on_attach)

        for i in range(GRID_LINES):
            line = []

            for j in range(GRID_COLS):
                cell = Cell(self.canvas, j, i)
                line.append(cell)

            self.cells.append(line)

    def on_fire(self, bubble):
        self.bubble = bubble

    def on_attach(self, cell, bubble):
        self.bubble = None

    def update(self):
        if self.bubble is not None:
            self.bubble.update()
            cell = grid_collision(self.cells, self.bubble)
            if cell:
                self.bubble.stop()
                cell.set_bubble(self.bubble)
                events.publish('attach', cell, self.bubble)
