from settings import COMMANDS, COMMANDS_COUNT, INJURIES, ACADEMIC_TITLES


def print_help_menu():
    print('''You can use the following commands,")
            by entering the command\'s number''')
    table = PrettyTable()
    table.field_names = ["Command", "Number"]
    for i in range(COMMANDS_COUNT):
        table.add_row([COMMANDS[i], str(i)])
    print(table)


def print_choose_academic_title():
    print("Choose one from the following academic titles:")
    for ac_title in ACADEMIC_TITLES:
        print(" - ", ac_title)


def print_choose_injuries():
    print("Choose one from the following injuries:")
    for injury in INJURIES:
        print(" - ", injury)


def print_for_updates(user):
    print("Set the {} data.".format(user))
    print("If you don\'t want to set some attribute, just write nothing.")
