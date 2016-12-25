from prettytable import PrettyTable
from settings import(
                    INJURIES,
                    ACADEMIC_TITLES,
                    COMMANDS,
                    COMMANDS_COUNT,
                    DOCTOR_COMMANDS,
                    DOCTOR_COMMANDS_COUNT,
                    PATIENT_COMMANDS,
                    PATIENT_COMMANDS_COUNT)


def print_start_menu(username, user_type):
    message = "Hi, {},\n".format(username)\
                + "You are a {} in Hospital Manager.\n".format(user_type)\
                + "You have the abilities to:\n"
    print(message)


def print_help_menu():
    print("Wellcome to Hospital Manager!\nChoose command.")
    for i in range(1, COMMANDS_COUNT + 1):
        print(str(i) + ') ' + COMMANDS[i])


def print_doctor_options():
    for i in range(DOCTOR_COMMANDS_COUNT):
        print(str(i) + ') ' + DOCTOR_COMMANDS[i])


def print_patient_options():
    for i in range(PATIENT_COMMANDS_COUNT):
        print(str(i) + ') ' + PATIENT_COMMANDS[i])


def print_choose_academic_title():
    print("Choose one from the following academic titles:")
    for ac_title in ACADEMIC_TITLES:
        print(" - ", ac_title)


def print_choose_injuries():
    print("Choose one from the following injuries:")
    for injury in INJURIES:
        print(" - ", injury)
