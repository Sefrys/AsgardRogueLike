import csv
import os.path


time = 5


def create_empty_highscore(filename="highscore.csv"):
    with open(filename, "w") as highscore_csv_file:
        highscore_file = csv.writer(highscore_csv_file, delimiter=",")
        header = ["Time [s]", "Name", "Class", "Lost HP"]
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


def fill_highscore(check, count, time, filename="highscore.csv"):
    header = ["Time [s]", "Name", "Class", "Lost HP"]
    name = ""
    hero_class = ""
    current_hero_stats = []
    with open("exportedNameClassHP.csv", "r") as current_hero_stats_csv:
        current_hero_stats_file = csv.reader(current_hero_stats_csv)
        for line in current_hero_stats_file:
            current_hero_stats.append(line[0])
        name = current_hero_stats[0]
        hero_class = current_hero_stats[1]
        lost_hp = current_hero_stats[2]
    with open(filename, "r") as highscore_csv_file:
        highscore_file = csv.reader(highscore_csv_file, delimiter=",")
        hero_score = [int(time), name, hero_class, lost_hp]
        highscore = []
        hero_score = [time, name, hero_class, lost_hp]
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


def display_highscore(filename="highscore.csv"):
    with open(filename, "r") as highscore_csv_file:
        highscore_file = csv.reader(highscore_csv_file, delimiter=",")
        highscore = []
        for line in highscore_file:
            highscore.append(line)

        row_lenght = 0
        for row in highscore[0]:
            for character in row:
                row_lenght += 1

        print("------HALL OF FAME------")
        print("_" * row_lenght)
        for row in highscore:
            print(*row)
        print("_" * row_lenght)


def main():
    # if not os.path.exists("highscore.csv"):
    #     create_empty_highscore()
    # check, count = check_highscore()
    # fill_highscore(check, count, time)
    display_highscore()


main()
