import pygame
import random
import datetime
import consts
import MineField

pygame.font.init()

Window_Name = pygame.display.set_caption("The Flag - Maya and Lihi")
WINDOW = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def drew_window(soldier):
    keys_pressed = pygame.key.get_pressed()
    WINDOW.fill(consts.WINDOW_COLOR)
    WINDOW.blit(consts.FLAG_IMAGE_RESIZE, (1150, 550))
    WINDOW.blit(consts.SOLIDER_IMAGE_RESIZE, (soldier.x, soldier.y))
    WINDOW.blit(consts.TEXT, (consts.TEXT_LOCATION))
    add_grass(grass_locations_list)
    pygame.display.update()


grass_locations_list = []
for i in range(20):
    x = random.randint(75, 1100)
    y = random.randint(125, 500)
    grass_location = (x, y)
    grass_locations_list.append(grass_location)


def add_grass(grass_locations_list):
    for i in range(len(grass_locations_list)):
        WINDOW.blit(consts.GRASS_IMAGE_RESIZE, (grass_locations_list[i][0], grass_locations_list[i][1]))

def lines():
    for i in range(50):
        pygame.draw.line(WINDOW, consts.NET_LINES_COLOR, (25 * i, 0), (25 * i, consts.WINDOW_HEIGHT), width=1)


def wide_lines():
    for j in range(25):
        pygame.draw.line(WINDOW, consts.NET_LINES_COLOR, (0, 25 * j), (consts.WINDOW_WIDTH, 25 * j), width=1)


NIGHT_WINDOW = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def drew_night_mode(soldier):
    sec_to_run = 1
    exec_end_time = datetime.datetime.now() + datetime.timedelta(seconds=sec_to_run)
    while True:
        WINDOW.fill(consts.NIGHT_MODE_WINDOW_COLOR)
        lines()
        wide_lines()
        MineField.add_bombs()
        WINDOW.blit(consts.NIGHT_SOLIDER_IMAGE_RESIZE, (soldier.x, soldier.y))
        pygame.display.update()
        if datetime.datetime.now() >= exec_end_time:
            break
