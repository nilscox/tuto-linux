import time
import tkinter
from cursor import Cursor
from cell import Cell

FPS = 16

top = tkinter.Tk()

canvas = tkinter.Canvas(top, bg="#424242", width=640, height=480)

cursor = Cursor(canvas, (320, 420))
cell = Cell(canvas, (42, 69))

canvas.pack()


while True:
    cursor.update()
    for bubble in cursor.bubbles:
        cell.check_collisions(bubble)
    top.update()
    time.sleep(1 / FPS)
