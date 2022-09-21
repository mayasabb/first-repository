import Bubble
import consts
import random
import Screen

stack = []


def create(stack_size):
    global stack
    stack = []
    for i in range(stack_size):
        add_bubble(i)
    return stack


def add_bubble(col):
    bubble_x = Bubble.calc_center_x(col, row=0,
                                    row_start=consts.STACK_LOCATION[0])
    stack.append(Bubble.create(bubble_x,
                               consts.STACK_LOCATION[1],
                               random.choice(consts.bubble_colors)))


def remove_first():
    bullet_bubble = stack.pop(0)

    for i in range(len(stack)):
        stack[i]["center_x"] = Bubble.calc_center_x(i, row=0,
                                                    row_start=
                                                    consts.STACK_LOCATION[0])
    return bullet_bubble


def get_length():
    return len(stack)


def draw():
    for bubble in stack:
        Screen.draw_bubble(bubble)

# -----------------------------------------------------------------------------
# ---------------------------------your code-----------------------------------
# -----------------------------------------------------------------------------

def get_stack_colors():
    stack_colors = []
    for bubble in stack:
        if bubble['color'] != consts.NO_BUBBLE:
            if bubble['color'] not in stack_colors:
                stack_colors.append(bubble['color'])
                return stack_colors

        ''''
    for row in range(get_length()):
        for col in range(consts.BUBBLE_GRID_COLS):
            bubble_color = bubbles_grid[row][col]['color']
            if bubble_color not in grid_colors:
                grid_colors.append(bubble_color)
    return grid_colors
'''