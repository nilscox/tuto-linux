from calculations import cell_box, cell_adjacent_cells, grid_cell_position


class Cell:

    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.position = grid_cell_position(x, y)
        self.bubble = None
        self.square = canvas.create_rectangle(*cell_box(self.position))
        canvas.create_text(self.position, text=str(', '.join(map(str, [x, y]))))

    def get_place(self):
        return self.x, self.y

    def get_position(self):
        return self.position

    def get_bubble(self):
        return self.bubble

    def get_bubble_color(self):
        if self.bubble is not None:
            return self.bubble.get_color()

    def set_bubble(self, bubble):
        if bubble is not None:
            bubble.set_position(self.position)

        self.bubble = bubble

    def get_adjacent(self, cells):
        return cell_adjacent_cells(cells, self.x, self.y)
