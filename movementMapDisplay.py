import os
import ast
import collections
import sys
import tty
import termios
import time
from rogueLike import fetch_current_time, game_end
from coldWarmHot import *
from combatEngine import *
from characterCreation import slow_print


def getch():
    '''Read key input without pressing enter'''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def generate_map(level="mapTest.txt"):
    '''Generates level map from separate file'''
    level_map = []
    with open(level, "r") as mapFile:
        for line in mapFile:
            for element in line:
                element.strip("")
            level_map.append(list(line.rstrip()))
    return level_map


def display_map(map_level):
    for char in map_level:
        print(*char)


def movement(start_time, map_level, hero_symbol="♦", wall_symbol=["◙", "#"],
             entrance_symbol="D", path_symbol=" ", cave_bat_symbol="&",
             wolf_symbol="☼", boss_symbol="%"):
    '''Hero movement (WSAD) and displays the level map on screen.'''
    damage_taken = 0
    hero_x_position = 1
    hero_y_position = 7
    hero_step = 1
    map_level[hero_y_position][hero_x_position] = hero_symbol
    next_map = False
    os.system('clear')
    while True:

        if next_map is True:
            map_level = generate_map("mapTwo.txt")
            movement(start_time, map_level, hero_symbol="♦", wall_symbol=["◙", "#"],
                     entrance_symbol="D", path_symbol=" ", cave_bat_symbol="&",
                     wolf_symbol="☼", boss_symbol="%")

        display_map(map_level)

        with open('classPlayer.py') as class_file:
            player_stats = ast.literal_eval(class_file.readline())

        player_stats = collections.OrderedDict(sorted(player_stats.items()))
        for attr, value, in player_stats.items():
            print('{} ---- {}'.format(attr, value))

        key = getch().lower()
        os.system('clear')

        if key == "w":
            if (not map_level[hero_y_position - hero_step][hero_x_position] in wall_symbol and
               not map_level[hero_y_position - hero_step][hero_x_position] == entrance_symbol):
                map_level[hero_y_position][hero_x_position] = path_symbol
                hero_y_position -= hero_step

        if key == "s":
            if (not map_level[hero_y_position + hero_step][hero_x_position] in wall_symbol and
               not map_level[hero_y_position + hero_step][hero_x_position] == entrance_symbol):
                map_level[hero_y_position][hero_x_position] = path_symbol
                hero_y_position += hero_step

        if key == "a":
            if (not map_level[hero_y_position][hero_x_position - hero_step] in wall_symbol and
               not map_level[hero_y_position][hero_x_position - hero_step] == entrance_symbol):
                map_level[hero_y_position][hero_x_position] = path_symbol
                hero_x_position -= hero_step

        if key == "d":
            if (not map_level[hero_y_position][hero_x_position + hero_step] in wall_symbol and
               not map_level[hero_y_position][hero_x_position + hero_step] == entrance_symbol):
                map_level[hero_y_position][hero_x_position] = path_symbol
                hero_x_position += hero_step
            if map_level[hero_y_position][hero_x_position + hero_step] in "→":
                next_map = True

        if map_level[hero_y_position][hero_x_position] == cave_bat_symbol:
            damage_taken += combat_core(damage_taken, monster_type=cave_bat, monster_name="Cave Bat")

        elif map_level[hero_y_position][hero_x_position] == wolf_symbol:
            damage_taken += combat_core(damage_taken, monster_type=wolf, monster_name="Wolf")

        elif map_level[hero_y_position][hero_x_position] == boss_symbol:
            with open('exportedNameClassHP.csv', 'a') as hp_export:
                hp_export.write("\n" + str(damage_taken) + "\n")
            string_boss_encounter = ("You encountered the big bad boss!" +
                                     "\nGuess what the three numbers are to win, or else, you'll die miserably!\n")
            slow_print(string_boss_encounter)
            initiate_how_warm_cold()
            game_end(start_time)
        map_level[hero_y_position][hero_x_position] = hero_symbol


def movement_core(start_time):
    '''Initializes movement and map display'''
    map_level = generate_map("mapOne.txt")
    movement(start_time, map_level)
