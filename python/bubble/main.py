import time
import tkinter
from cursor import Cursor

FPS = 16

top = tkinter.Tk()

canvas = tkinter.Canvas(top, bg="#424242", width=640, height=480)

cursor = Cursor(canvas, (320, 420))

canvas.pack()


while True:
    cursor.update()
    top.update()
    time.sleep(1 / FPS)
