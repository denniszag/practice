from enum import Enum
from MissileLauncher import MissileLauncher
from missiles import *


class Actions(Enum):
    STORE = 1
    LAUNCH = 2
    REPORT = 3
    DEL = 4
    EXIT = 5


def print_menu():
    print("Actions:")
    print("\t{} - Store new missile".format(Actions.STORE.value))
    print("\t{} - Launch missile".format(Actions.LAUNCH.value))
    print("\t{} - Inventory report".format(Actions.REPORT.value))
    print("\t{} - clean out missile".format(Actions.DEL.value))
    print("\t{} - Exit".format(Actions.EXIT.value))


def get_missile(name):

    if name.lower() == "ballistic":
        return Ballistic()
    elif name.lower() == "torpedo":
        return Torpedo()
    elif name.lower() == "cruise":
        return Cruise()
    elif name.lower() == "long":
        return LongDistance()
    return None


def number_input() -> int:

    while True:
        try:
            number = int(input())
            return number
        except ValueError:
            print("please insert a number")


def start():
    print("Welcome")
    print_menu()
    action_id = number_input()
    launcher = MissileLauncher()

    while action_id != Actions.EXIT.value:

        if action_id == Actions.STORE.value:
            print("Enter missile type")
            new_missile_type = input()
            new_missile = get_missile(new_missile_type)
            if new_missile:
                launcher.add_to_supply(new_missile)
            else:
                print("no such missile type")
        elif action_id == Actions.LAUNCH.value:
            print("Enter missile index")
            missile_index = input()
            if missile_index.lower() == "totalwar":
                missile_index = -1

            try:
                missile_index = int(missile_index)
                launch_result = launcher.launch(missile_index)
                if launch_result > 0:
                    print("{} missiles launched".format(launch_result))
                elif launch_result == -1:
                    print("no such index")
                else:
                    print("Failed!")
            except ValueError:
                print("not a valid input")

        elif action_id == Actions.DEL.value:
            print("Enter missile index")
            missile_index = number_input()
            remove_result = launcher.remove_from_supply(missile_index)
            if remove_result:
                print("removed")
            else:
                print("no such index for missile")
        elif action_id == Actions.REPORT.value:
            print(launcher.full_report())

        else:
            print("please insert valid action")

        print_menu()
        action_id = number_input()


if __name__ == '__main__':
    start()
