import events


class ScoreManager:

    def __init__(self, win_callback):
        self.win_callback = win_callback

        events.subscribe('pop', self.on_pop)

    def on_pop(self, bubbles):
        self.win_callback(1)
