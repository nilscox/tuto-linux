import time
import tkinter

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from game import Game

FPS = 32


def start(root, game):
    last_update = time.time()

    while True:
        now = time.time()

        game.update(now - last_update)
        root.update()

        last_update = now
        time.sleep(1 / FPS)


def main():
    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, bg="#424242", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    game = Game(canvas)
    start(root, game)

    root.quit()


if __name__ == '__main__':
    main()
