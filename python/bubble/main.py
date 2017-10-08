import time
import tkinter

from game import Game

FPS = 16

top = tkinter.Tk()

canvas = tkinter.Canvas(top, bg="#424242", width=640, height=480)
canvas.pack()

game = Game(canvas)


while True:
    game.update()
    top.update()
    time.sleep(1 / FPS)
