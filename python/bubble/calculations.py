from math import sin, cos, atan, sqrt

import events
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


def bubble_box(position):
    x, y = position

    x0, y0 = x - BUBBLE_RADIUS, y - BUBBLE_RADIUS
    x1, y1 = x + BUBBLE_RADIUS, y + BUBBLE_RADIUS

    return x0, y0, x1, y1


def cell_box(position):
    x, y = position
    hsize = CELL_SIZE / 2

    x0, y0 = x - hsize, y - hsize
    x1, y1 = x + hsize, y + hsize

    return x0, y0, x1, y1


def cell_adjacent_cells(cells, x, y):
    return []


def grid_collision(cells, bubble):

    def get_closest_cell():
        x, y = bubble.get_position()

        def distance(cell):
            cx, cy = cell.get_position()
            dx, dy = x - cx, y - cy
            return cell, sqrt(dx * dx + dy * dy)

        m = None
        cell = None

        for line in cells:
            for (c, d) in map(distance, line):
                if cell is None or d < m:
                    m = d
                    cell = c

        return cell

    def grid_collision_walls():
        first = cells[0][0]
        last = cells[GRID_LINES - 1][GRID_COLS - 1]
        hsize = CELL_SIZE / 2
        bx0, by0, bx1, by1 = bubble_box(bubble.get_position())

        x0, y0 = first.get_position()
        x0, y0 = x0 - hsize, y0 - hsize

        x1, y1 = last.get_position()
        x1 += hsize

        return bx0 < x0 or by0 < y0 or bx1 > x1

    def grid_collision_cells():

        def bubbles_intersection(b1, b2):
            bx1, by1 = b1.get_position()
            bx2, by2 = b2.get_position()
            dx, dy = bx2 - bx1, by2 - by1

            d = sqrt(dx * dx + dy * dy)

            return d <= 2 * BUBBLE_RADIUS

        for line in cells:
            for cell in line:
                cbubble = cell.get_bubble()
                if cbubble and bubbles_intersection(bubble, cbubble):
                    return True

        return False

    if grid_collision_walls() or grid_collision_cells():
        cell = get_closest_cell()
        cell.set_bubble(bubble)
        events.publish('attach')


def grid_cell_position(x, y):
    offset = CELL_SIZE / 2 if y % 2 else 0
    return CELL_SIZE + CELL_SIZE * x + offset, CELL_SIZE + CELL_SIZE * y
