from datetime import datetime, date
import csv
from os import path


directory_path = path.dirname(path.realpath(__file__))


# Reads dates from birthdays.csv
# Assigns them to birthdays dictionary
def init_dictionary() -> dict:
    birthdays = {}
    # birthdays.csv is the file birthdays are written in
    # example :

    # name1,day/month
    # name2,day/month
    # ...
    with open(f"{directory_path}/birthdays.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            # row[0] is date, row[1] is name
            birthdays[f"{row[0]}"] = row[1]

    return birthdays


# Return the closest birthday and remaining time
def closest_birthday(birthdays: dict) -> list:

    # Selecting the first values to compare
    closest_date = list(birthdays.keys())[0]
    closest_name = list(birthdays.values())[0]

    # Get the distance between today and the first date to compare
    remaining_time = abs(
        datetime.strptime(f"{closest_date}/{datetime.today().year}", "%d/%m/%Y") - datetime.today())

    for key, value in birthdays.items():

        difference = abs(datetime.today() -
                         datetime.strptime(f"{key}/{datetime.today().year}", "%d/%m/%Y"))

        # If the distance between iterated date and today is smaller than the one before, switch them.
        if difference < remaining_time:

            remaining_time = difference

            closest_date = key
            closest_name = value

    # Getting rid of the decimal point (miliseconds)
    return [closest_date, closest_name, str(remaining_time).split('.')[0]]


def main() -> None:
    birthdays = init_dictionary()
    closest = closest_birthday(birthdays)

    print(f"Closest birthday : {closest[1]}'s Birthday in {closest[0]}")
    print(f"Remaining time : {closest[2]}")


if __name__ == "__main__":
    main()
