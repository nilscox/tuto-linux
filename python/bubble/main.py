import time
import tkinter

from constants import CANVAS_WIDTH, CANVAS_HEIGHT
from game import Game

FPS = 16

top = tkinter.Tk()

canvas = tkinter.Canvas(top, bg="#424242", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

game = Game(canvas)


while True:
    game.update()
    top.update()
    time.sleep(1 / FPS)
