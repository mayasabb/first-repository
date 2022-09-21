import consts
import Screen
import random

bombs_locations_list = []
bomb_tuples_list = []
bombs_field_location_list = []

for i in range(20):
    x = random.randrange(75, 1125, 25)
    y = random.randrange(125, 525, 25)
    bombs_location = (x, y)
    bombs_locations_list.append(bombs_location)
    bombs_field_location = [y // 25, x // 25]
    bombs_field_location_list.append(bombs_field_location)
print(bombs_field_location_list)


def add_bombs():
    for j in range(len(bombs_locations_list)):
        Screen.WINDOW.blit(consts.BOMB_IMAGE_RESIZE, (bombs_locations_list[j][0], bombs_locations_list[j][1]))


def check_bomb_indexes():
    bomb_indexes = []
    for i in range(len(bombs_field_location_list)):
        next_to_bomb_1 = [bombs_field_location_list[i][0], bombs_field_location_list[i][1] + 1]
        next_to_bomb_2 = [bombs_field_location_list[i][0], bombs_field_location_list[i][1] + 2]

        bomb_indexes.append(bombs_field_location_list[i])
        bomb_indexes.append(next_to_bomb_1)
        bomb_indexes.append(next_to_bomb_2)

    return bomb_indexes
print(check_bomb_indexes())







