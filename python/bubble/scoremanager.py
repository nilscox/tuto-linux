import events


class ScoreManager:

    def __init__(self):
        self.combo_points = 0

        events.subscribe('pop', self.on_pop)
        events.subscribe('detach', self.on_detach)

    def win_points(self, points):
        events.publish('win_points', points)

    def on_pop(self, bubbles):
        nbubbles = len(bubbles)

        if nbubbles == 0:
            self.combo_points = 0
        else:
            self.combo_points += nbubbles
            self.win_points(self.combo_points)

    def on_detach(self, bubbles):
        self.win_points(sum(range(len(bubbles) + 1)))
