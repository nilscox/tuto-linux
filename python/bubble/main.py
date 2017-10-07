import time
import tkinter
from cursor import Cursor
from grid import Grid

FPS = 16

top = tkinter.Tk()

canvas = tkinter.Canvas(top, bg="#424242", width=640, height=480)

cursor = Cursor(canvas, (320, 420))
grid = Grid(canvas)

canvas.pack()


while True:
    grid.update()
    top.update()
    time.sleep(1 / FPS)
