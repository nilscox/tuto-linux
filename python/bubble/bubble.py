from random import choice
from calculations import bubble_box
from constants import BUBBLE_COLORS, BUBBLE_SPEED


class Bubble:

    def __init__(self, canvas, position):
        self.position = position
        self.canvas = canvas
        self.direction = None
        self.speed = 8
        self.color = choice(BUBBLE_COLORS)
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
        self.set_position((x + dx * BUBBLE_SPEED, y + dy * BUBBLE_SPEED))

    def die(self):
        self.canvas.delete(self.circle)

    def update(self, ellapsed):
        if self.direction is None:
            return

        dx, dy = self.direction
        direction = dx * ellapsed, dy * ellapsed

        self.move(direction)
