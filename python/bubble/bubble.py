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

    def update(self):
        x, y = self.position
        dx, dy = self.direction
        x, y = x + dx * self.speed, y + dy * self.speed
        self.position = (x, y)
        x0, y0 = x - RADIUS, y - RADIUS
        x1, y1 = x + RADIUS, y + RADIUS
        self.canvas.coords(self.circle, x0, y0, x1, y1)

    def on_click(self, event):
        x0, y0 = event.x - RADIUS, event.y - RADIUS
        x1, y1 = event.x + RADIUS, event.y + RADIUS
        self.canvas.coords(self.circle, x0, y0, x1, y1)
