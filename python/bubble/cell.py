from calculations import cell_position


class Cell:

    def __init__(self, canvas, position):
        self.position = position
        self.bubble = None
        self.square = canvas.create_rectangle(*cell_position(self.position))

    def get_position(self):
        return self.position

    def set_bubble(self, bubble):
        bubble.stop()
        bubble.set_position(self.position)
        self.bubble = bubble
