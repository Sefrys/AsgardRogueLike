import sys
import time
from characterCreation import slow_print


def introduction_title():
    ''' prints game title in ascii '''
    game_title = open('gameTitle.txt', "r")
    print_game_name = game_title.read()
    slow_print(print_game_name, 0.0005)
    game_title.close()
    time.sleep(1)
