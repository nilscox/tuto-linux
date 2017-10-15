import events


class ScoreManager:

    def __init__(self, win_callback):
        self.win_callback = win_callback

        events.subscribe('pop', self.on_pop)
        events.subscribe('detach', self.on_detach)

    def on_pop(self, bubbles):
        self.win_callback(len(bubbles))

    def on_detach(self, bubbles):
        self.win_callback(sum(range(len(bubbles))))
