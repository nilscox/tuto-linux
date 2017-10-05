from math import sin, cos, atan, sqrt
from constants import *


def cursor_position(angle):
    x, y = CURSOR_POSITION
    x0, y0 = x - CURSOR_LENGTH * sin(angle), y - CURSOR_LENGTH * cos(angle)
    x1, y1 = x + CURSOR_LENGTH * sin(angle), y + CURSOR_LENGTH * cos(angle)

    return x0, y0, x1, y1


def cursor_fire_direction(direction):
    x, y = direction
    l = sqrt(x * x + y * y)

    return x / l, y / l


def cursor_angle(direction):
    dx, dy = direction
    return atan(dx / dy)


def bubble_position(position):
    x, y = position

    x0, y0 = x - BUBBLE_RADIUS, y - BUBBLE_RADIUS
    x1, y1 = x + BUBBLE_RADIUS, y + BUBBLE_RADIUS

    return x0, y0, x1, y1


def cell_position(position):
    x, y = position
    hsize = CELL_SIZE / 2

    x0, y0 = x - hsize, y - hsize
    x1, y1 = x + hsize, y + hsize

    return x0, y0, x1, y1


def cell_bubble_collision(cell, bubble):
    x0, y0, x1, y1 = cell_position(cell.get_position())
    bx, by = bubble.get_position()

    return x0 < bx < x1 and y0 < by < y1


def grid_cells():
    return GRID_LINES * GRID_COLS


def grid_cell_position(n):
    x, y = n % GRID_COLS, int(n / GRID_COLS)

    return CELL_SIZE + CELL_SIZE * x, CELL_SIZE + CELL_SIZE * y
