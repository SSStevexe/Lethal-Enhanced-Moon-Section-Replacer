from enum import Enum


class UserAction:
    class Action(Enum):
        MODIFY_RARITIES = 1
        REPLACE_SECTION = 2
        EXIT_SCRIPT = 3

    def get_user_action(self) -> int:
        print("Select an action to perform:\n")
        print("1. Modify rarities for scraps or monsters in all moons.")
        print("2. Replace a section of moons by risk level")
        print("3. Exit script")

        while True:
            user_input = input("Enter the number of the action you would like to perform: ")
            try:
                user_action = int(user_input)
                if self.Action(user_action) in self.Action.__members__.values():
                    return user_action
                else:
                    print("Invalid action. Please enter a valid action.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")
