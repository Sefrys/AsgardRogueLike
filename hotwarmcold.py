def hotwarmcold():

    print("""Let's play a game. Ruls are very easy. I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
      Cold       No digit is correct.
      Warm       One digit is correct but in the wrong position.
      Hot        One digit is correct and in the right position.
    I have thought up a number. You have 10 guesses to get it.\n""")

    while True:
        try:
            first_digit = int(input("type a first digit : "))
            if first_digit in range(0, 10):
                break
            else:
                print("Digit is ONE digit NIGGA! ")
                continue
        except ValueError:
            print("DIGIT, DO YAH NOW WAT DAT IS MEAN, NIGGA!?")
    while True:
        try:
            second_digit = int(input("type a second digit : "))
            if second_digit in range(0, 10):
                break
            else:
                print("Digit is ONE digit NIGGA! ")
                continue
        except ValueError:
            print("Really!? Da same problem NIGGA!!")
    while True:
        try:
            third_digit = int(input("type a third digit : "))
            if third_digit in range(0, 10):
                break
            else:
                print("Digit is ONE digit NIGGA! ")
                continue
        except ValueError:
            print("All right you are to stupid to play this game. HASTA LA VISTA DUSHBAG")
            quit()
    secret_number = (first_digit, second_digit, third_digit)

    guess_number = 1

    while guess_number < 11:
        print("Guess #", guess_number)
        guess_list = []
        guess = input("Enter the correct number: ")

        for i in guess:
            for j in secret_number:
                if int(i) == j:
                    if guess.index(i) == secret_number.index(j):
                        guess_list.insert(0, "hot")
                    else:
                        guess_list.append("warm")
        if guess_list == ["hot", "hot", "hot"]:
            print("You win!!!")
            break
        if guess != secret_number and guess_list == []:
            guess_list.append("cold")
        print(guess_list)
        guess_number += 1
    if guess_number == 11:
        print("You lost! ....LOSER")
