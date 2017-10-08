import events
from bubble import Bubble
from constants import CURSOR_POSITION
from calculations import cursor_position, cursor_angle, cursor_fire_direction

SIZE = 42


class Cursor:

    def __init__(self, canvas):
        self.canvas = canvas
        self.position = CURSOR_POSITION
        self.angle = 0
        self.next_bubble = Bubble(self.canvas, self.position)
        self.can_fire = True

        self.line = canvas.create_line(*cursor_position(self.angle), width=4)
        canvas.bind('<Motion>', self.on_mousemove)
        canvas.bind('<Button-1>', self.on_click)

        events.subscribe('attach', self.on_bubble_attach)

    def on_bubble_attach(self):
        self.can_fire = True

    def fire(self, direction):
        if not self.can_fire:
            return

        bubble = self.next_bubble
        self.next_bubble = Bubble(self.canvas, self.position)
        self.can_fire = False

        bubble.set_direction(direction)
        events.publish('fire', bubble)

    def on_mousemove(self, event):
        x, y = self.position
        direction = event.x - x, event.y - y
        self.angle = cursor_angle(direction)
        self.canvas.coords(self.line, *cursor_position(self.angle))

    def on_click(self, event):
        x, y = self.position
        direction = event.x - x, event.y - y
        self.fire(cursor_fire_direction(direction))
