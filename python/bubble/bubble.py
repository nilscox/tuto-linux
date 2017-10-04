from calculations import bubble_position

RADIUS = 20


class Bubble:

    def __init__(self, canvas, position, direction, color):
        self.canvas = canvas
        self.position = position
        self.direction = direction
        self.speed = 8

        x, y = position
        x0, y0 = x - RADIUS, y - RADIUS
        x1, y1 = x + RADIUS, y + RADIUS

        self.circle = canvas.create_oval(x0, y0, x1, y1, fill=color, width=0)

    def set_position(self, position):
        self.canvas.coords(self.circle, *bubble_position(position))
        self.position = position

    def move(self, direction):
        dx, dy = direction
        x, y = self.position
        self.set_position((x + dx * self.speed, y + dy * self.speed))

    def update(self):
        self.move(self.direction)

    def on_click(self, event):
        x0, y0 = event.x - RADIUS, event.y - RADIUS
        x1, y1 = event.x + RADIUS, event.y + RADIUS
        self.canvas.coords(self.circle, x0, y0, x1, y1)
