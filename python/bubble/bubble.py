from random import choice
from calculations import bubble_position

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
        self.circle = canvas.create_oval(*bubble_position(self.position), fill=choice(COLORS), width=0)

    def set_position(self, position):
        self.canvas.coords(self.circle, *bubble_position(position))
        self.position = position

    def set_direction(self, direction):
        self.direction = direction

    def move(self, direction):
        dx, dy = direction
        x, y = self.position
        self.set_position((x + dx * self.speed, y + dy * self.speed))

    def update(self):
        if self.direction is None:
            return

        self.move(self.direction)
