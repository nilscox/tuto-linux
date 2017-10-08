from calculations import cell_position, cell_adjacent_cells, grid_cell_position


class Cell:

    def __init__(self, canvas, position, place):
        self.position = position
        self.place = place
        self.bubble = None
        self.square = canvas.create_rectangle(*cell_position(self.position))
        canvas.create_text(self.position, text=str(self.place))

    def get_position(self):
        return self.position

    def get_bubble(self):
        return self.bubble

    def set_bubble(self, bubble):
        bubble.stop()
        bubble.set_position(self.position)
        self.bubble = bubble

    def get_adjacent(self, cells):
        return cell_adjacent_cells(cells, self.place)
