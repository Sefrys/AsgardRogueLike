import sys
import time


def slow_print(string, delay=.001):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)


def introduction_title():
    ''' prints game title in ascii '''
    game_title = open('gameTitle.txt', "r")
    print_game_name = game_title.read()
    slow_print(print_game_name)
    game_title.close()
    time.sleep(1)
