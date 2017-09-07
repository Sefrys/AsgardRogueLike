import os
import ast
import collections
import sys
import tty
import termios
from combatEngine import *


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


def movement(map_level, hero_symbol="♦", wall_symbol=["◙", "#"],
             entrance_symbol="D", path_symbol=" ", cave_bat_symbol="&",
             wolf_symbol="☼"):

    '''Hero movement (WSAD) and displays the level map on screen.'''
    hero_x_position = 1
    hero_y_position = 7
    hero_step = 1
    map_level[hero_y_position][hero_x_position] = hero_symbol
    next_map = False
    os.system('clear')
    while True:

        if next_map is True:
            map_level = generate_map("mapTwo.txt")
            movement(map_level)

        display_map(map_level)

        with open('classPlayer.py') as class_file:
            player_stats = ast.literal_eval(class_file.readline())

        player_stats = collections.OrderedDict(sorted(player_stats.items()))
        for attr, value, in player_stats.items():
            print('{} ---- {}'.format(attr, value))

        key = getch()
        os.system('clear')

        # emergency exit
        if key == "q":
            exit()

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
            combat_core(monster_type=cave_bat, monster_name="Cave Bat")

        elif map_level[hero_y_position][hero_x_position] == wolf_symbol:
            combat_core(monster_type=wolf, monster_name="Wolf")

        map_level[hero_y_position][hero_x_position] = hero_symbol

def movement_core():
    '''Initializes movement and map display'''
    map_level = generate_map("mapOne.txt")
    movement(map_level)
