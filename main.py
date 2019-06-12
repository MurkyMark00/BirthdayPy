from datetime import datetime, date
import csv


class Birthday():

    def __init__(self) -> None:
        self.birthdays: dict = {}
        self.init_dictionary()

    # Reads dates from birthdays.csv
    # Assigns them to self.birthdays
    def init_dictionary(self) -> None:
        with open("Desktop/Scripts/BirthdaysPy/birthdays.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                # row[0] is date, row[1] is name
                self.birthdays[f"{row[0]}"] = row[1]

    # Return the closest birthday and remaining time
    def closest_birthday(self):

        # Selecting the first values to compare
        closest_date = list(self.birthdays.keys())[0]
        closest_name = list(self.birthdays.values())[0]

        # Get the distance between today and the first date to compare
        remaining_time = abs(
            datetime.strptime(f"{closest_date}/{datetime.today().year}", "%d/%m/%Y") - datetime.today())

        for key, value in self.birthdays.items():

            # If the distance between iterated date and today is smaller than the one before, switch them.
            if abs(datetime.today() - datetime.strptime(f"{key}/{datetime.today().year}", "%d/%m/%Y")) < remaining_time:

                remaining_time = abs(
                    datetime.today() - datetime.strptime(f"{key}/{datetime.today().year}", "%d/%m/%Y"))

                closest_date = key
                closest_name = value

        return [closest_date, closest_name, str(remaining_time).split('.')[0]]


def main():
    birthday_object = Birthday()
    closest_birthday = birthday_object.closest_birthday()

    print(
        f"Closest birthday : {closest_birthday[1]}'s Birthday in {closest_birthday[0]}\nRemaining time : {closest_birthday[2]}")


if __name__ == "__main__":
    main()
