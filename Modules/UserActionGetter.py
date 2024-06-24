from enum import Enum


class MainActions(Enum):
    MODIFY_RARITIES = 1
    REPLACE_SECTION = 2
    EXIT_SCRIPT = 3


class ScrapOrMonster(Enum):
    SCRAP = 1
    MONSTER = 2


def get_user_action() -> int:
    print("Select an action to perform:\n")
    print("1. Modify rarities for scraps or monsters in all moons.")
    print("2. Replace a section of moons by risk level")
    print("3. Exit script")

    while True:
        user_input = input("Enter the number of the action you would like to perform: ")
        try:
            user_action = int(user_input)
            if MainActions(user_action) in MainActions.__members__.values():
                return user_action
            else:
                print("Invalid action. Please enter a valid action.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def get_scrap_or_monster_replacement_action() -> int:
    print("Select an action to perform:\n")
    print("1. Update scrap rarities")
    print("2. Update monster rarities")
    while True:
        user_input = input("Enter the number of the action you would like to perform: ")
        try:
            user_action = int(user_input)
            if ScrapOrMonster(user_action) in ScrapOrMonster.__members__.values():
                return user_action
            else:
                print("Invalid action. Please enter a valid action.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
