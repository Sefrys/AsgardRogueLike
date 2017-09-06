from gameBoard import *
from classPlayer import *
import os

def getch():
    import sys, tty, termios
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
            levelMap.append(list(line.rstrip()))
    return levelMap


def movement_hero(mapLevel, hero_symbol="☺", wall_symbol=["≈", "#"],
                  entrance_symbol="D", path_symbol=" "):
    x_hero = 2
    y_hero = 7
    hero_step = 1
    mapLevel[y_hero][x_hero] = hero_symbol
    os.system('clear')
    while True:
        for i in mapLevel:
            print(*i)

        for attr, value, in player_attr.items():
            print('{} ---- {}'.format(attr, value))
        key = getch()
        os.system('clear')
        if key == "q":
            break

        if key == "w":
            if (not mapLevel[y_hero - hero_step][x_hero] in wall_symbol and
               not mapLevel[y_hero - hero_step][x_hero] == entrance_symbol):
                mapLevel[y_hero][x_hero] = path_symbol
                y_hero -= hero_step

        if key == "s":
            if (not mapLevel[y_hero + hero_step][x_hero] in wall_symbol and
               not mapLevel[y_hero + hero_step][x_hero] == entrance_symbol):
                mapLevel[y_hero][x_hero] = path_symbol
                y_hero += hero_step

        if key == "a":
            if (not mapLevel[y_hero][x_hero - hero_step] in wall_symbol and
               not mapLevel[y_hero][x_hero - hero_step] == entrance_symbol):
                mapLevel[y_hero][x_hero] = path_symbol
                x_hero -= hero_step

        if key == "d":
            if (not mapLevel[y_hero][x_hero + hero_step] in wall_symbol and
               not mapLevel[y_hero][x_hero + hero_step] == entrance_symbol):
                mapLevel[y_hero][x_hero] = path_symbol
                x_hero += hero_step

        mapLevel[y_hero][x_hero] = hero_symbol
        # --- MAKE MAP SMALLER, FORMAT THE STAT SIZE



def movement_core():
    mapLevel = generate_map("mapMaze.txt")

    movement_hero(mapLevel)
