import events


class ScoreManager:

    def __init__(self):
        events.subscribe('pop', self.on_pop)
        events.subscribe('detach', self.on_detach)

    def win_points(self, points):
        events.publish('win_points', points)

    def on_pop(self, bubbles):
        self.win_points(len(bubbles))

    def on_detach(self, bubbles):
        self.win_points(sum(range(len(bubbles) + 1)))
