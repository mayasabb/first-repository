import pygame
import os
pygame.font.init()


WINDOW_WIDTH = 1250
WINDOW_HEIGHT = 625
WINDOW_COLOR = (63, 164, 77)
FPS = 60
SIZE_OF_SQUARE = 25
FIELD_ROWS = 25
FIELD_COLS = 50

SOLIDER_IMAGE = pygame.image.load(os.path.join('soldier.png'))
SOLIDER_WIDTH = 50
SOLIDER_HEIGHT = 100
SOLIDER_IMAGE_RESIZE = pygame.transform.scale(SOLIDER_IMAGE, (SOLIDER_WIDTH, SOLIDER_HEIGHT))

GRASS_IMAGE = pygame.image.load(os.path.join('grass.png'))
GRASS_WIDTH = 75
GRASS_HEIGHT = 50
GRASS_IMAGE_RESIZE = pygame.transform.scale(GRASS_IMAGE, (GRASS_WIDTH, GRASS_HEIGHT))

FLAG_IMAGE = pygame.image.load(os.path.join('flag.png'))
FLAG_WIDTH = 100
FLAG_HEIGHT = 100
FLAG_IMAGE_RESIZE = pygame.transform.scale(FLAG_IMAGE, (FLAG_WIDTH, FLAG_HEIGHT))

NET_LINES_COLOR = (77, 255, 77)
NIGHT_MODE_WINDOW_COLOR = (0, 0, 0)


TEXT_COLOR = (255, 255, 255)
TEXT_FONT = pygame.font.SysFont('comicsans', 20)
TEXT = TEXT_FONT.render("Welcome to the flag game. Have Fun!", True, TEXT_COLOR)
TEXT_LOCATION = (2 * SIZE_OF_SQUARE + 10, 0)

WIN_TEXT_FONT = pygame.font.SysFont('comicsans', 200)
WIN_TEXT = TEXT_FONT.render("YOU WON!", True, TEXT_COLOR)
WIN_TEXT_LOCATION = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

LOSE_TEXT_FONT = pygame.font.SysFont('comicsans', 200)
LOSE_TEXT = TEXT_FONT.render("YOU LOST!", True, TEXT_COLOR)
LOSE_TEXT_LOCATION = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

BOMB_IMAGE = pygame.image.load(os.path.join('mine.png'))
BOMB_WIDTH = 75
BOMB_HEIGHT = 25
BOMB_IMAGE_RESIZE = pygame.transform.scale(BOMB_IMAGE, (BOMB_WIDTH, BOMB_HEIGHT))

NIGHT_SOLIDER_IMAGE = pygame.image.load(os.path.join('soldier_nigth.png'))
NIGHT_SOLIDER_WIDTH = 50
NIGHT_SOLIDER_HEIGHT = 100
NIGHT_SOLIDER_IMAGE_RESIZE = pygame.transform.scale(NIGHT_SOLIDER_IMAGE, (NIGHT_SOLIDER_WIDTH, NIGHT_SOLIDER_HEIGHT))

EXP_IMAGE = pygame.image.load(os.path.join('explotion.png'))
EXP_WIDTH = 800
EXP_HEIGHT = 550
EXP_IMAGE_RESIZE = pygame.transform.scale(EXP_IMAGE, (EXP_WIDTH, EXP_HEIGHT))
EXP_LOCATION = (300, 100)

