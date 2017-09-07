import random
import sys
import time
from characterCreation import slow_print


def get_random_digits():
    correct_answer = []
    while len(correct_answer) < 3:
        digit = random.randint(0, 9)
        if digit not in correct_answer:
            correct_answer.append(digit)
    return correct_answer


def get_user_input():
    while True:
        user_guess = input("Enter a number: ")
        if user_guess.isalpha():
            print("Enter only digits")
        elif len(user_guess) != 3:
            print("You have to enter exactly 3 digits!")
        else:
            return list(user_guess)


def compare_user_input_with_answer(user_guess, correct_answer):
    index = 0
    hint_list = []
    for a in correct_answer:
        if str(a) == user_guess[index]:
            hint_list.insert(0, 'HOT')
        elif str(a) in user_guess:
            hint_list.append("WARM")
        index += 1
    if not hint_list:
        hint_list.append("COLD")

    return hint_list


def check_result(hint_list):
    if hint_list == ["HOT"] * 3:
        return True


def initiate_how_warm_cold():
    correct_answer = get_random_digits()
    tries_left = 10

    while tries_left > 0:
        user_guess = get_user_input()
        result = compare_user_input_with_answer(user_guess, correct_answer)
        print(" ".join(result))
        if check_result(result):
            string_victory = ("\nYou perform a courageous attack and strike the monster down!" +
                              "\nCongratulations! You are victorious and can go home!\n")
            slow_print(string_victory, 0.02)
            time.sleep(2)
            exit()
        tries_left -= 1

    if tries_left == 0:
        string_loss = ("\nThe monster rips you to shreds." +
                       "\nGame over :(\n")
        slow_print(string_loss, 0.02)
        time.sleep(2)
        exit()
