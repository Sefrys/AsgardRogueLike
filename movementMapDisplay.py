import os
import ast
import collections
import sys
import tty
import termios
from combatEngine import *


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def generate_map(level="mapTest.txt"):
    levelMap = []
    with open(level, "r") as mapFile:
        for line in mapFile:
            for element in line:
                element.strip("")
            levelMap.append(list(line.rstrip()))
    return levelMap


def movement_hero(mapLevel, hero_symbol="♦", wall_symbol=["◙", "#"],
                  entrance_symbol="D", path_symbol=" ", monster_symbol="&"):

    step_count = 0
    hero_x_position = 1
    hero_y_position = 7
    hero_step = 1
    mapLevel[hero_y_position][hero_x_position] = hero_symbol
    os.system('clear')
    while True:

        with open('classPlayer.py') as class_file:
            player_stats = ast.literal_eval(class_file.readline())

        player_stats = collections.OrderedDict(sorted(player_stats.items()))
        for attr, value, in player_stats.items():
            print('{} ---- {}'.format(attr, value))

        for i in mapLevel:
            print(*i)

        key = getch()
        os.system('clear')
        if key == "q":
            break

        if key == "w":
            if (not mapLevel[hero_y_position - hero_step][hero_x_position] in wall_symbol and
               not mapLevel[hero_y_position - hero_step][hero_x_position] == entrance_symbol):
                mapLevel[hero_y_position][hero_x_position] = path_symbol
                hero_y_position -= hero_step

        if key == "s":
            if (not mapLevel[hero_y_position + hero_step][hero_x_position] in wall_symbol and
               not mapLevel[hero_y_position + hero_step][hero_x_position] == entrance_symbol):
                mapLevel[hero_y_position][hero_x_position] = path_symbol
                hero_y_position += hero_step

        if key == "a":
            if (not mapLevel[hero_y_position][hero_x_position - hero_step] in wall_symbol and
               not mapLevel[hero_y_position][hero_x_position - hero_step] == entrance_symbol):
                mapLevel[hero_y_position][hero_x_position] = path_symbol
                hero_x_position -= hero_step

        if key == "d":
            if (not mapLevel[hero_y_position][hero_x_position + hero_step] in wall_symbol and
               not mapLevel[hero_y_position][hero_x_position + hero_step] == entrance_symbol):
                mapLevel[hero_y_position][hero_x_position] = path_symbol
                hero_x_position += hero_step

        if mapLevel[hero_y_position][hero_x_position] == monster_symbol:
            combat_core()

        mapLevel[hero_y_position][hero_x_position] = hero_symbol


def movement_core():
    mapLevel = generate_map("mapMaze.txt")
    movement_hero(mapLevel)
