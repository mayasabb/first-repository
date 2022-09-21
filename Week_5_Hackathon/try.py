import pygame
import os
pygame.font.init()

WINDOW_WIDTH =820
WINDOW_HEIGHT = 600
WINDOW_COLOR = (255, 255, 255)
WINDOW = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT))

PANEL_PHOTO = pygame.image.load(os.path.join('PANELS.jpg'))
PANEL_PHOTO_WIDTH = 820
PANEL_PHOTO_HEIGHT = 600
PANEL_PHOTO_RESIZE = pygame.transform.scale(PANEL_PHOTO, (PANEL_PHOTO_WIDTH, PANEL_PHOTO_HEIGHT))

TEXT_COLOR = (0, 0, 0)
TEXT_FONT = pygame.font.SysFont('timesnewroman', 50)
TEXT = TEXT_FONT.render("Welcome to the flag game. Have Fun!", True, TEXT_COLOR)
TEXT_LOCATION = (20, 250)


def drew_window():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys_pressed = pygame.key.get_pressed()
            WINDOW.fill(WINDOW_COLOR)
            WINDOW.blit(PANEL_PHOTO_RESIZE, (0, 0))
            WINDOW.blit(TEXT, (TEXT_LOCATION))
            pygame.display.update()

    pygame.quit()

if __name__ == "__try__":
    drew_window()

drew_window()