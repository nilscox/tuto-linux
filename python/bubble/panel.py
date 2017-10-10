from calculations import panel_box, panel_center


class Panel:

    def __init__(self, canvas, text):
        self.canvas = canvas
        self.square = canvas.create_rectangle(*panel_box(), fill='grey', width=1)
        self.text = canvas.create_text(panel_center(), text=text, fill='black')
