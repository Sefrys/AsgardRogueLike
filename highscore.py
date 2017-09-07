import csv


time = 35
name = "Filipeq"
hero_class = "mage"
hero_hp = 15


def create_empty_highscore(filename="highscore.csv"):
    with open(filename, "w") as highscore_csv_file:
        highscore_file = csv.writer(highscore_csv_file, delimiter=",")
        header = ["Time", "Name", "Class", "HP"]
        highscore_file.writerow(header)


def check_highscore(filename="highscore.csv"):
    with open(filename, "r") as highscore_file:
        count = 0
        max_number_of_lines = 11
        for line in highscore_file:
            count += 1

        if count < max_number_of_lines:
            return True, count
        else:
            return False, count


def fill_highscore(check, count, time, name, hero_class, hero_hp, filename="highscore.csv"):
    header = ["Time", "Name", "Class", "HP"]

    with open(filename, "r") as highscore_csv_file:
        highscore_file = csv.reader(highscore_csv_file, delimiter=",")
        hero_score = [int(time), name, hero_class, hero_hp]
        highscore = []
        hero_score = [time, name, hero_class, hero_hp]
        for line in highscore_file:
            highscore.append(line)

    if check:

        with open(filename, "w") as highscore_csv_file:
            highscore_file = csv.writer(highscore_csv_file, delimiter=",")
            highscore_file.writerow(header)
            only_scores = []
            for i in range(1, len(highscore)):
                only_scores.append(highscore[i])
            only_scores.append(hero_score)
            highscore = sorted(only_scores, key=lambda x: int(x[0]))
            print(highscore)
            for line in highscore:
                highscore_file.writerow(line)
    else:

        with open(filename, "w") as highscore_csv_file:
            highscore_file = csv.writer(highscore_csv_file, delimiter=",")
            highscore_file.writerow(header)
            del highscore[-1]
            only_scores = []
            for i in range(1, len(highscore)):
                only_scores.append(highscore[i])
            only_scores.append(hero_score)
            highscore = sorted(only_scores, key=lambda x: int(x[0]))
            print(highscore)
            for line in highscore:
                highscore_file.writerow(line)


def main():
    # create_empty_highscore()
    check, count = check_highscore()
    fill_highscore(check, count, time, name, hero_class, hero_hp)


main()
