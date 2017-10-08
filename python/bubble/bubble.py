from random import choice
from calculations import bubble_box

RADIUS = 20
COLORS = [
    'red',
    'green',
    'blue',
    'yellow',
    'purple',
    'brown',
    'pink',
]


class Bubble:

    def __init__(self, canvas, position):
        self.position = position
        self.canvas = canvas
        self.direction = None
        self.speed = 8
        self.color = choice(COLORS)
        self.circle = canvas.create_oval(*bubble_box(self.position), fill=self.color, width=0)

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.canvas.coords(self.circle, *bubble_box(position))
        self.position = position

    def set_direction(self, direction):
        self.direction = direction

    def stop(self):
        self.direction = None

    def move(self, direction):
        dx, dy = direction
        x, y = self.position
        self.set_position((x + dx * self.speed, y + dy * self.speed))

    def update(self):
        if self.direction is None:
            return

        self.move(self.direction)
