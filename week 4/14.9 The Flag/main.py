import Screen
import pygame
import consts
import Soldier
import time
import Database

soldier = pygame.Rect(0, 0, consts.SOLIDER_WIDTH, consts.SOLIDER_HEIGHT)
list_of_nums = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]


def main():
    # list_of_nums = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
    row = 0
    col = 0
    global soldier
    soldier = pygame.Rect(0, 0, consts.SOLIDER_WIDTH, consts.SOLIDER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        Screen.drew_window(soldier)
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Screen.drew_night_mode(soldier)
            for i in range(len(list_of_nums)):
                if event.type == pygame.KEYDOWN:
                    if event.key == list_of_nums[i]:
                        t = time.time()
                if event.type == pygame.KEYUP:
                    if event.key == list_of_nums[i]:
                        t = time.time() - t;t = str(t);t = t[:5]
                        t = float(t)
                        if t < 1:
                            Database.saving_info_from_game(i)
                            # print("You pressed less than a second!")
                        if t > 1:
                            # df = Database.saving_info_from_game(i)
                            Database.reading_info_to_game(i)
                            # print("You pressed more than a second!")

            new_location = Soldier.soldier_movement(soldier, row, col)
            row = new_location[0]
            col = new_location[1]

            if event.type == pygame.KEYDOWN:
                consts.TEXT = consts.TEXT_FONT.render("", True, consts.TEXT_COLOR)
                pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()