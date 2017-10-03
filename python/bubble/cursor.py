from math import sin, cos, atan, sqrt
from bubble import Bubble

SIZE = 42


class Cursor:

    def __init__(self, canvas, position):
        self.canvas = canvas
        self.position = position
        self.angle = 0
        self.bubble = None

        x, y = position
        x0, y0 = x - SIZE * sin(self.angle), y - SIZE * cos(self.angle)
        x1, y1 = x + SIZE * sin(self.angle), y + SIZE * cos(self.angle)

        self.line = canvas.create_line(x0, y0, x1, y1, width=4)
        canvas.bind('<Motion>', self.on_move)
        canvas.bind('<Button-1>', self.on_click)

    def fire(self, x, y):
        l = sqrt(x * x + y * y)
        x, y = x / l, y / l
        self.bubble = Bubble(self.canvas, self.position, (x, y), 'blue')

    def update(self):
        if self.bubble is not None:
            self.bubble.update()

    def on_move(self, event):
        x, y = self.position
        ex, ey = event.x, event.y
        dx, dy = ex - x, ey - y

        self.angle = atan(dx / dy)

        x0, y0 = x - SIZE * sin(self.angle), y - SIZE * cos(self.angle)
        x1, y1 = x + SIZE * sin(self.angle), y + SIZE * cos(self.angle)

        self.canvas.coords(self.line, x0, y0, x1, y1)

    def on_click(self, event):
        x, y = self.position
        ex, ey = event.x, event.y
        dx, dy = ex - x, ey - y

        self.fire(dx, dy)
