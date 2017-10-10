import events
from bubble import Bubble
from constants import GRID_LINES, GRID_COLS, CELLS_TOUCHING_THRESHOLD, GRID_INITIAL_LINES
from calculations import grid_collision
from cell import Cell


def create_line(canvas, i):
    line = []

    for j in range(GRID_COLS):
        cell = Cell(canvas, j, i)

        if i <= GRID_INITIAL_LINES - 1:
            cell.set_bubble(Bubble(canvas, (0, 0)))

        line.append(cell)

    return line


class Grid:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cells = []
        self.bubble = None

        events.subscribe('fire', self.on_fire)
        events.subscribe('attach', self.on_attach)

        for i in range(GRID_LINES):
            self.cells.append(create_line(self.canvas, i))

    def on_fire(self, bubble):
        self.bubble = bubble

    def on_attach(self, cell, bubble):
        self.bubble = None

        def check_color(cell, path):
            path.append(cell)

            for c in cell.get_adjacent(self.cells):
                if c in path:
                    continue

                if c.get_bubble_color() == bubble.get_color():
                    check_color(c, path)

            return path

        cells = check_color(cell, [])

        if len(cells) >= CELLS_TOUCHING_THRESHOLD:
            for cell in cells:
                cell.get_bubble().die()
                cell.set_bubble(None)

    def spawn_line(self):
        self.cells.pop()
        self.cells.insert(0, create_line(self.canvas, 0))

        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                self.cells[i][j].set_place(j, i)

    def get_last_line(self):
        return self.cells[len(self.cells) - 1]

    def update(self, ellapsed):
        if self.bubble is not None:
            self.bubble.update(ellapsed)
            cell = grid_collision(self.cells, self.bubble)
            if cell:
                self.bubble.stop()
                cell.set_bubble(self.bubble)
                events.publish('attach', cell, self.bubble)
