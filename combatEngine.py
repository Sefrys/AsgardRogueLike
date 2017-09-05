import os
import random
import time
from classPlayer import *
from classMonsters import *


def monster_combat_stats(monster_type):
    monster_derived_stats = {"HP": 0, "ACC": 0, "EVA": 0}

    monster_derived_stats["HP"] = monster_type["STA"]*2
    monster_derived_stats["ACC"] = monster_type["DEX"]*1.8
    monster_derived_stats["EVA"] = monster_type["DEX"]*1.3

    return(monster_derived_stats)


def player_combat_stats():
    player_derived_stats = {"HP": 0, "ACC": 0, "EVA": 0}

    player_derived_stats["HP"] = player_attr["STA"]*2
    player_derived_stats["ACC"] = player_attr["DEX"]*1.8
    player_derived_stats["EVA"] = player_attr["DEX"]*1.3

    return(player_derived_stats)


def combat_ui(monster_name, player_derived_stats, monster_derived_stats,
              monster_type, dice_12_roll, dice_20_roll, dice_6_roll):
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
                print("GAME OVER")
                break
        else:
            print("Invalid input, try again.\n")


def combat_sequence(player_derived_stats, monster_derived_stats, monster_type, dice_12_roll, dice_20_roll, dice_6_roll):

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
                monster_HP -= damage_roll
                print("Player HP: ", player_HP)
                print("Opponent HP: ", monster_HP)
                print("You dealt " + str(damage_roll) + " damage to the opponent!")
                time.sleep(1.5)
                os.system('clear')
            else:
                print("Player HP: ", player_HP)
                print("Opponent HP: ", monster_HP)
                print("Your attack missed!")
                time.sleep(1.5)
                os.system('clear')
            # --- Victory decision
            if monster_HP <= 0:
                print("Player HP: ", player_HP)
                print("Opponent HP: ", monster_HP)
                print("You killed the monster")
                time.sleep(1.5)
                os.system('clear')
                break
            else:
                player_turn = False
        elif player_turn is False:
            monster_hit_accuracy = monster_ACC + dice_12_roll()
            monster_miss_chance = player_EVA + dice_12_roll()
            if monster_hit_accuracy > monster_miss_chance:
                damage_roll = monster_type["STR"] - dice_6_roll()
                player_HP -= damage_roll
                print("Player HP: ", player_HP)
                print("Opponent HP: ", monster_HP)
                print("The monster hits you for " + str(damage_roll) + " damage!")
                time.sleep(1.5)
                os.system('clear')
            else:
                print("Player HP: ", player_HP)
                print("Opponent HP: ", monster_HP)
                print("You dodged the monster attack!")
                time.sleep(1.5)
                os.system('clear')
            # --- Loss decision
            if player_HP <= 0:
                print("Player HP: ", player_HP)
                print("Opponent HP: ", monster_HP)
                print("You are defeated")
                time.sleep(1.5)
                os.system('clear')
                player_status = "defeated"
                break
            else:
                player_turn = True


def dice_20_roll():
    d20_roll = random.randint(1, 21)
    return(d20_roll)


def dice_12_roll():
    d12_roll = random.randint(1, 13)
    return(d12_roll)


def dice_6_roll():
    d6_roll = random.randint(1, 7)
    return(d6_roll)


def combat_core():
    monster_type = cave_bat
    monster_name = cave_bat_name
    monster_derived_stats = monster_combat_stats(monster_type)
    player_derived_stats = player_combat_stats()
    combat_ui(monster_name, player_derived_stats, monster_derived_stats,
              monster_type, dice_12_roll, dice_20_roll, dice_6_roll)
