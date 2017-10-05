from calculations import cell_position, cell_bubble_collision


class Cell:

    def __init__(self, canvas, position):
        self.position = position
        self.bubble = None
        self.square = canvas.create_rectangle(*cell_position(self.position))

    def get_position(self):
        return self.position

    def check_collisions(self, bubble):
        if cell_bubble_collision(self, bubble):
            bubble.stop()
            bubble.set_position(self.position)

            self.bubble = bubble
