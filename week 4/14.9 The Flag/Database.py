import consts
import MineField
import Screen
import Soldier
import main
import pandas as pd


def soldier_location(soldier):
    soldier_location1 = [soldier.x, soldier.y]
    return soldier_location1


soldier_loc = soldier_location(main.soldier)
grass_loc = Screen.grass_locations_list
bomb_loc = MineField.bombs_locations_list


def saving_info_from_game(i):
    data = {
        'X Soldier': [soldier_loc[0]],
        'Y Soldier': [soldier_loc[1]],
        'Grass List': [grass_loc],
        'Bomb List': [bomb_loc]
    }

    df = pd.DataFrame(data, index=[i + 1])

    df.to_csv('file1.csv', mode='a')

    return df


def reading_info_to_game(i):

    data1 = pd.read_csv("file1.csv")
    row = data1.loc[i]
    print(row)
    # print(data1.to_string(df.loc[i]))


#print(reading_info_to_game())
