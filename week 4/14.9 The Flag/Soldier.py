import MineField
import consts
import pygame
import Screen
import datetime
pygame.font.init()


def soldier_movement(soldier, row, col):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_DOWN] and (soldier.y + consts.SIZE_OF_SQUARE + consts.SOLIDER_HEIGHT) <= consts.WINDOW_HEIGHT:
        soldier.y += consts.SIZE_OF_SQUARE
        row += 1
        col += 0
        location = [row, col]
        body_location = checking_soldier_body(location)
        check_if_win(body_location)
        check_if_lost(location)
    if keys_pressed[pygame.K_UP] and (soldier.y - consts.SIZE_OF_SQUARE) >= 0:
        soldier.y -= consts.SIZE_OF_SQUARE
        row -= 1
        col += 0
        location = [row, col]
        body_location = checking_soldier_body(location)
        check_if_win(body_location)
        check_if_lost(location)
    if keys_pressed[pygame.K_LEFT] and (soldier.x - consts.SIZE_OF_SQUARE) >= 0:
        soldier.x -= consts.SIZE_OF_SQUARE
        row += 0
        col -= 1
        location = [row, col]
        body_location = checking_soldier_body(location)
        check_if_win(body_location)
        check_if_lost(location)
    if keys_pressed[pygame.K_RIGHT] and (soldier.x + consts.SIZE_OF_SQUARE + consts.SOLIDER_WIDTH) <= consts.WINDOW_WIDTH:
        soldier.x += consts.SIZE_OF_SQUARE
        row += 0
        col += 1
        location = [row, col]
        body_location = checking_soldier_body(location)
        check_if_win(body_location)
        check_if_lost(location)

    location = [row, col]
    return location


def checking_soldier_body(location):
    soldier_body = []
    soldier_body.append((location[0] + 1, location[1]))
    soldier_body.append((location[0] +1, location[1] +1))
    print("soldier body list", soldier_body)
    return soldier_body


def checking_soldier_legs(location):
    soldier_legs = []
    soldier_legs.append([location[0] + 3, location[1]])
    soldier_legs.append([location[0] + 3, location[1] + 1])
    print("solder legs list", soldier_legs)
    return soldier_legs


def check_if_win(body_location):
    flag_good_indexes = [(22, 46), (22, 47), (22, 48)]
    for i in range(len(flag_good_indexes)):
        if body_location[0] == flag_good_indexes[i]:
            sec_to_run = 3
            exec_end_time = datetime.datetime.now() + datetime.timedelta(seconds=sec_to_run)
            while True:
                Screen.WINDOW.blit(consts.WIN_TEXT, (consts.WIN_TEXT_LOCATION))
                pygame.display.update()
                if datetime.datetime.now() >= exec_end_time:
                    break
            pygame.quit()

def check_if_lost(location):
    legs = checking_soldier_legs(location)
    bomb = MineField.check_bomb_indexes()
    for i in range(len(bomb)):
        if legs[0] == bomb[i] or legs[1] == bomb[i]:
            sec_to_run = 3
            exec_end_time = datetime.datetime.now() + datetime.timedelta(seconds=sec_to_run)
            while True:
                Screen.WINDOW.blit(consts.EXP_IMAGE_RESIZE, consts.EXP_LOCATION)
                Screen.WINDOW.blit(consts.LOSE_TEXT, (consts.LOSE_TEXT_LOCATION))
                pygame.display.update()
                if datetime.datetime.now() >= exec_end_time:
                    break
            pygame.quit()




