import events
from bubble import Bubble
from constants import CURSOR_POSITION, CURSOR_BUBBLES_LOOKAHEAD
from calculations import cursor_position, cursor_angle, cursor_fire_direction, cursor_bubble_position

SIZE = 42


class Cursor:

    def __init__(self, canvas):
        self.canvas = canvas
        self.position = CURSOR_POSITION
        self.angle = 0
        self.next_bubbles = []
        self.can_fire = True

        for i in range(CURSOR_BUBBLES_LOOKAHEAD):
            bubble = Bubble(self.canvas, cursor_bubble_position(self.position, i))
            self.next_bubbles.append(bubble)

        self.line = canvas.create_line(*cursor_position(self.angle), width=4)
        canvas.bind('<Motion>', self.on_mousemove)
        canvas.bind('<Button-1>', self.on_click)

        events.subscribe('attach', self.on_bubble_attach)
        events.subscribe('lost', self.on_lost)

    def on_bubble_attach(self, cell, bubble):
        self.can_fire = True

    def on_lost(self):
        self.can_fire = False

    def fire(self, direction):
        if not self.can_fire:
            return

        bubble = self.next_bubbles.pop(0)
        self.next_bubbles.append(Bubble(self.canvas, self.position))
        self.can_fire = False

        for i in range(CURSOR_BUBBLES_LOOKAHEAD):
            self.next_bubbles[i].set_position(cursor_bubble_position(self.position, i))

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
