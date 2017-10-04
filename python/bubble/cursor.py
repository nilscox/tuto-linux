from bubble import Bubble
from calculations import cursor_position, cursor_angle, cursor_fire_direction

SIZE = 42


class Cursor:

    def __init__(self, canvas, position):
        self.canvas = canvas
        self.position = position
        self.angle = 0
        self.bubble = None

        self.line = canvas.create_line(*cursor_position(self.angle), width=4)
        canvas.bind('<Motion>', self.on_mousemove)
        canvas.bind('<Button-1>', self.on_click)

    def fire(self, direction):
        self.bubble = Bubble(self.canvas, self.position, direction, 'blue')

    def update(self):
        if self.bubble is not None:
            self.bubble.update()

    def on_mousemove(self, event):
        x, y = self.position
        direction = event.x - x, event.y - y
        self.angle = cursor_angle(direction)
        self.canvas.coords(self.line, *cursor_position(self.angle))

    def on_click(self, event):
        x, y = self.position
        direction = event.x - x, event.y - y
        self.fire(cursor_fire_direction(direction))
