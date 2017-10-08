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


def cell_bubble_collision(cells, cell, bubble):
    x0, y0, x1, y1 = cell_position(cell.get_position())
    bx, by = bubble.get_position()

    return x0 < bx < x1 and y0 < by < y1


def get_closest_cell(cells, bubble):
    bx, by = bubble.get_position()

    def distance(cell):
        cx, cy = cell.get_position()
        dx, dy = bx - cx, by - cy
        return cell, sqrt(dx * dx + dy * dy)

    m = None
    cell = None

    for (c, d) in map(distance, cells):
        if cell is None or d < m:
            m = d
            cell = c

    return cell


def grid_bubble_collision_walls(cells, bubble):
    first = cells[0]
    last = cells[len(cells) - 1]
    hsize = CELL_SIZE / 2
    bx0, by0, bx1, by1 = bubble_position(bubble.get_position())

    x0, y0 = first.get_position()
    x0, y0 = x0 - hsize, y0 - hsize

    x1, y1 = last.get_position()
    x1 += hsize

    return bx0 < x0 or by0 < y0 or bx1 > x1


def grid_bubble_intersect(cells, bubble):
    first = cells[0]
    last = cells[len(cells) - 1]
    hsize = CELL_SIZE / 2
    bx0, by0, bx1, by1 = bubble_position(bubble.get_position())

    x0, y0 = first.get_position()
    x0, y0 = x0 - hsize, y0 - hsize

    x1, y1 = last.get_position()
    x1, y1 = x1 + hsize, y1 + hsize

    return bx0 < x0 or by0 < y0 or bx1 > x1 or by1 > y1


def bubble_bubble_intersect(b1, b2):
    bx1, by1 = b1.get_position()
    bx2, by2 = b2.get_position()
    dx, dy = bx2 - bx1, by2 - by1

    d = sqrt(dx * dx + dy * dy)

    return d <= 2 * BUBBLE_RADIUS


def grid_bubble_collision_cells(cells, bubble):
    if grid_bubble_intersect(cells, bubble):
        return

    for cell in cells:
        cbubble = cell.get_bubble()
        if cbubble and bubble_bubble_intersect(bubble, cbubble):
            return True

    return False


def grid_bubble_collision(cells, bubble):
    cell = get_closest_cell(cells, bubble)
    if grid_bubble_collision_walls(cells, bubble) or grid_bubble_collision_cells(cells, bubble):
        cell.set_bubble(bubble)
        events.publish('attach')


def grid_cells():
    return GRID_LINES * GRID_COLS


def grid_cell_position(n):
    x, y = n % GRID_COLS, int(n / GRID_COLS)

    return CELL_SIZE + CELL_SIZE * x, CELL_SIZE + CELL_SIZE * y
