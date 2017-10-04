from calculations import bubble_position

RADIUS = 20


class Bubble:

    def __init__(self, canvas, position, direction, color):
        self.canvas = canvas
        self.position = position
        self.direction = direction
        self.speed = 8
        self.circle = canvas.create_oval(*bubble_position(self.position), fill=color, width=0)

    def set_position(self, position):
        self.canvas.coords(self.circle, *bubble_position(position))
        self.position = position

    def move(self, direction):
        dx, dy = direction
        x, y = self.position
        self.set_position((x + dx * self.speed, y + dy * self.speed))

    def update(self):
        self.move(self.direction)
