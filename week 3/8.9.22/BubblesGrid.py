import math

import consts
import Bubble
import random
import Screen

bubbles_grid = []


def create():
    global bubbles_grid
    bubbles_grid = [
        create_bubble_row(row, row_start=0, row_length=consts.BUBBLE_GRID_COLS)
        for row in
        range(consts.BUBBLE_GRID_START_ROWS)]

    # Create an empty row for future bubbles
    last_row = consts.BUBBLE_GRID_START_ROWS
    bubbles_grid.append(create_empty_row(last_row))


def create_empty_row(row_number):
    return [Bubble.create(Bubble.calc_center_x(col, row_number, 0),
                          Bubble.calc_center_y(row_number),
                          consts.NO_BUBBLE)
            for col in range(consts.BUBBLE_GRID_COLS)]


def put_bubble_in_grid(bubble, location):
    bubbles_grid[location[0]][location[1]]["color"] = bubble["color"]


def should_bubbles_pop(same_color_cluster):
    return len(same_color_cluster) >= consts.MIN_CLUSTER_SIZE_TO_POP


# Returns a list of the locations in the bubbles grid that are a part of the
# cluster
# TODO: make an inner function
def get_same_color_cluster(start_location, color, locations_checked):
    start_row, start_col = start_location
    locations_checked.append(start_location)
    neighbors_directions = get_neighbors_directions(start_row)

    if bubbles_grid[start_row][start_col]["color"] != color:
        return []

    same_color_cluster = [start_location]

    for direction in neighbors_directions:
        new_row = start_row + direction[0]
        new_col = start_col + direction[1]
        new_location = (new_row, new_col)

        if 0 <= new_row < len(bubbles_grid) and \
                0 <= new_col < consts.BUBBLE_GRID_COLS and \
                new_location not in locations_checked:
            same_color_cluster += get_same_color_cluster(new_location,
                                                         color,
                                                         locations_checked)

    return same_color_cluster


def get_neighbors_directions(row_number):
    neighbors_directions = [(0, -1), (0, + 1)]

    if row_number % 2 == 0:
        neighbors_directions += [(-1, -1), (-1, 0), (1, -1), (1, 0)]
    else:
        neighbors_directions += [(-1, 0), (-1, 1), (1, 0), (1, 1)]

    return neighbors_directions


def pop_bubbles(bubbles_to_pop_locations):
    bubbles_popped = []
    for bubble_location in bubbles_to_pop_locations:
        bubbles_popped.append(Bubble.pop(bubbles_grid, bubble_location))

    return bubbles_popped


def animate_bubbles_pop(bubbles_popping):
    bubbles_popping[0]["radius"] -= consts.BUBBLE_SMALLER_BY
    if bubbles_popping[0]["radius"] <= 0:
        bubbles_popping.remove(bubbles_popping[0])


# Deletes last empty lines after the last line. One last line should always be
# empty, but no more than that
def delete_last_empty_lines(num_of_lines_to_delete):
    last_line_index = len(bubbles_grid) - 1

    for row in range(last_line_index, last_line_index - num_of_lines_to_delete,
                     -1):
        bubbles_grid.pop(row)


def is_line_empty(line):
    for bubble in line:
        if bubble["color"] != consts.NO_BUBBLE:
            return False

    return True


def count_empty_lines():
    num_of_empty_lines = 0

    for row in range(len(bubbles_grid) - 1, -1, -1):
        if is_line_empty(bubbles_grid[row]):
            num_of_empty_lines += 1
        else:
            break

    return num_of_empty_lines


def set_one_empty_line():
    num_of_empty_lines = count_empty_lines()

    # There should always be exactly one empty line
    if num_of_empty_lines == 0:
        bubbles_grid.append(create_empty_row(row_number=len(bubbles_grid)))
    else:
        delete_last_empty_lines(num_of_empty_lines - 1)


def create_bubble_row(row_index, row_start, row_length):
    return [Bubble.create(Bubble.calc_center_x(col, row_index, row_start),
                          Bubble.calc_center_y(row_index),
                          random.choice(consts.bubble_colors)) for col in
            range(row_length)]


def add_first_line():
    bubbles_grid.insert(0, create_bubble_row(row_index=0, row_start=0,
                                             row_length=consts.BUBBLE_GRID_COLS))


def recalc_bubbles_locations():
    # There is no need to do so for the first line, since it was just added
    for row in range(1, len(bubbles_grid)):
        for col in range(consts.BUBBLE_GRID_COLS):
            bubbles_grid[row][col]["center_x"] = Bubble.calc_center_x(col, row,
                                                                      row_start=0)
            bubbles_grid[row][col]["center_y"] = Bubble.calc_center_y(row)


def add_new_line():
    add_first_line()
    recalc_bubbles_locations()


def get_length():
    return len(bubbles_grid)


def draw():
    for row in bubbles_grid:
        for bubble in row:
            if bubble["color"] != consts.NO_BUBBLE:
                Screen.draw_bubble(bubble)


# -----------------------------------------------------------------------------
# ---------------------------------your code-----------------------------------
# -----------------------------------------------------------------------------

def find_bubble_location_in_grid(bullet_bubble):
    min_dist = Bubble.calc_dist(bullet_bubble, get_bubble(0,0))
    index_to_insert = (0,0)
    for row in range(len(bubbles_grid)):
        for col in range(len(bubbles_grid[row])):
            bubble = bubbles_grid[row][col]
            if bubble["color"] == consts.NO_BUBBLE:
                dist = Bubble.calc_dist(bullet_bubble, bubble)
                if dist < min_dist:
                    min_dist = dist
                    index_to_insert = (row, col)
                #bullet_bubble_point = (bullet_bubble["center_x"], bullet_bubble["center_y"])
                #bubble_point = (bubble["center_x"], bubble["center_y"])
                #distance = math.dist(bullet_bubble_point, bubble_point)

                #if distance <= 2 * consts.BUBBLE_RADIUS:
                    return (index_to_insert)

    '''
    for row in range(len(bubbles_grid)):
        for col in range(len(bubbles_grid[row])):
            bubble = bubbles_grid[row][col]
            if bubble["color"] != consts.NO_BUBBLE:
                min_dist = Bubble.calc_dist(bullet_bubble,bubble)
                min_dist_list = []
                min_dist_list.append(min_dist)
                if min_dist < min_dist_list[0]:
                    bubble['color'] = bullet_bubble['color']
                    bubble_tuple = (bubbles_grid[row],bubbles_grid[col])
                    min_dist_list.remove(min_dist_list[0])
                return bubble_tuple
    '''


def find_isolated_bubbles():
    isolated_bubbles_list = []
    for row in range(get_length()):
        for col in range(consts.BUBBLE_GRID_COLS):
            bubble = get_bubble(row, col)
            if bubble['color'] != consts.NO_BUBBLE:
                if Bubble.is_isolated(bubbles_grid, bubble):
                    isolated_bubbles_list.append(row, col)
        return isolated_bubbles_list


def get_bubble(row, col):
    return bubbles_grid[row][col]

def get_grid_colors():
    grid_colors = []
    for row in range(get_length()):
        for col in range(consts.BUBBLE_GRID_COLS):
            bubble_color = bubbles_grid[row][col]['color']
            if bubble_color not in grid_colors:
                grid_colors.append(bubble_color)
    return grid_colors