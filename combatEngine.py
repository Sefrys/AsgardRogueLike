import os
import random
import time
import ast
from gameOverDisplay import *
from classMonsters import *


def wait():
    '''Waits for enter input'''
    input("\nPress enter to continue")


def monster_combat_stats(monster_type):
    '''Derive combat attributes from basic attributes attributes'''
    monster_derived_stats = {"HP": 0, "ACC": 0, "EVA": 0}

    monster_derived_stats["HP"] = monster_type["STA"]*2
    monster_derived_stats["ACC"] = monster_type["DEX"]*2
    monster_derived_stats["EVA"] = monster_type["DEX"]*1.3

    return(monster_derived_stats)


def player_combat_stats():
    '''Derive combat attributes from retrieved basic player attributes'''
    with open('classPlayer.py') as class_file:
        player_attr = ast.literal_eval(class_file.readline())

    player_derived_stats = {"HP": 0, "ACC": 0, "EVA": 0}

    player_derived_stats["HP"] = player_attr["STA"]*2
    player_derived_stats["ACC"] = player_attr["DEX"]*2
    player_derived_stats["EVA"] = player_attr["DEX"]*1.3

    return(player_derived_stats)


def encounter_ui(monster_name, player_derived_stats, monster_derived_stats,
                 monster_type, dice_12_roll, dice_20_roll, dice_6_roll):
    '''Open screen with choices upon monster encounter'''
    os.system('clear')
    print("You've encountered a " + monster_name + "!\n")
    encounter_choices = ["FIGHT", "RUN", "GIVE UP"]
    while True:
        encounter_choice = input("Your options:\n - Fight\n - Run\n - Give Up\nWhat will you do?: ").upper()
        if encounter_choice.isalpha() and encounter_choice in encounter_choices:
            if encounter_choice == "FIGHT":
                os.system('clear')
                combat_sequence(player_derived_stats, monster_derived_stats,
                                monster_type, dice_12_roll, dice_20_roll, dice_6_roll)
                break
            elif encounter_choice == "RUN":
                print("Coward!")
                break
            elif encounter_choice == "GIVE UP":
                game_over()
                wait()
                exit()
        else:
            print("Invalid input, try again.\n")


def combat_sequence(player_derived_stats, monster_derived_stats, monster_type,
                    dice_12_roll, dice_20_roll, dice_6_roll):
    '''Combat sequence: first both monster and player roll for initiative,
        the one with the highest initiative starts first.
        Attribute checks are rolled (accuracy vs. evasion).
        if evasion > acc, it's a miss. Otherwise, a damage roll is performed
        and the damage is subtracted from the HP pool.
        Turns are repeated until someone dies.'''

    with open('classPlayer.py') as class_file:
        player_attr = ast.literal_eval(class_file.readline())

    # get monster and player combat stats
    monster_HP = monster_derived_stats["HP"]
    monster_ACC = monster_derived_stats["ACC"]
    monster_EVA = monster_derived_stats["EVA"]

    player_HP = player_derived_stats["HP"]
    player_ACC = player_derived_stats["ACC"]
    player_EVA = player_derived_stats["EVA"]

    # --- initiative rolls ---
    player_initiative = dice_20_roll()
    monster_initiative = dice_20_roll()

    if player_initiative >= monster_initiative:
        player_turn = True
    else:
        player_turn = False

    while True:
        if player_turn is True:
            player_hit_accuracy = player_ACC + dice_12_roll()
            player_miss_chance = monster_EVA + dice_12_roll()
            if player_hit_accuracy > player_miss_chance:
                damage_roll = player_attr["STR"] - dice_6_roll()
                if damage_roll > 0:
                    monster_HP -= damage_roll
                print("Player HP: " + str(player_HP) + "\nOpponent HP: " + str(monster_HP))
                if damage_roll > 0:
                    print("You dealt " + str(damage_roll) + " damage to the opponent!")
                else:
                    print("You dealt no damage!")
                    wait()
                os.system('clear')
            else:
                print("Player HP: " + str(player_HP) + "\nOpponent HP: " + str(monster_HP))
                print("Your attack missed!")
                wait()
                os.system('clear')
            # --- Victory decision
            if monster_HP <= 0:
                print("Player HP: " + str(player_HP) + "\nOpponent HP: " + str(monster_HP))
                print("You killed the monster")
                wait()
                os.system('clear')
                break
            else:
                player_turn = False
        elif player_turn is False:
            monster_hit_accuracy = monster_ACC + dice_12_roll()
            monster_miss_chance = player_EVA + dice_12_roll()
            if monster_hit_accuracy > monster_miss_chance:
                damage_roll = monster_type["STR"] - dice_6_roll()
                if damage_roll > 0:
                    player_HP -= damage_roll
                print("Player HP: " + str(player_HP) + "\nOpponent HP: " + str(monster_HP))
                if damage_roll > 0:
                    print("The monster hits you for " + str(damage_roll) + " damage!")
                else:
                    print("The monster dealt no damage!")
                    wait()
                os.system('clear')
            else:
                print("Player HP: " + str(player_HP) + "\nOpponent HP: " + str(monster_HP))
                print("You dodged the monster attack!")
                wait()
                os.system('clear')
            # --- Loss decision
            if player_HP <= 0:
                print("Player HP: " + str(player_HP) + "\nOpponent HP: " + str(monster_HP))
                print("You are defeated")
                wait()
                os.system('clear')
                game_over()
                wait()
                exit()
            else:
                player_turn = True


def dice_20_roll():
    '''Twenty sided dice thrown, returning the result'''
    d20_roll = random.randint(1, 21)
    return(d20_roll)


def dice_12_roll():
    '''Twelve sided dice thrown, returning the result'''
    d12_roll = random.randint(1, 13)
    return(d12_roll)


def dice_6_roll():
    '''Six sided dice thrown, returning the result'''
    d6_roll = random.randint(1, 7)
    return(d6_roll)


def combat_core(monster_type=None, monster_name=None):
    '''Main function executing the whole combat scenario'''
    monster_derived_stats = monster_combat_stats(monster_type)
    player_derived_stats = player_combat_stats()
    encounter_ui(monster_name, player_derived_stats, monster_derived_stats,
                 monster_type, dice_12_roll, dice_20_roll, dice_6_roll)
