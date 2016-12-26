import os
import sys
import getpass
from hospital_data_base import HospitalDB
from doctor import Doctor
from patient import Patient
from populate_starting_data import populate_hospital, is_hospital_existing
from settings import COMMANDS_COUNT
from password import encode
from validations import validate_password
from helper_prints import(
                        print_help_menu,
                        print_choose_injuries,
                        print_choose_academic_title)


class HospitalManager:
    def __init__(self, hospital_name):
        hospital_name = hospital_name.replace(' ', '-')
        db_was_not_existing = not(is_hospital_existing(hospital_name))
        self.hospital = HospitalDB(hospital_name)
        self.commands = self.__make_function_dict()
        # only if there was no database with this name, we populate it with data
        if db_was_not_existing:
            populate_hospital(self.hospital)

    def run_interface(self):
        while True:
            os.system('clear')
            self.__start_menu()
            try:
                command = int(input("command:> "))
                self.__execute_command(command)
            except ValueError:
                input("Wrong input: No such command.\n" +
                        "Press Enter to continue...")

    def __execute_command(self, command):
        try:
            if command in range(1, COMMANDS_COUNT + 1):
                self.commands[command]()
            else:
                print("Wrong input: No such command.")
        except ValueError as err:
            print("Wrong input: ", err)
        input("Press Enter to continue...")

    def __login(self):
        username = input("username:> ")
        password = getpass.getpass("password:> ")
        self.hospital.login_user(username, password)

    def __register(self):
        username = input("username:> ")
        password = getpass.getpass("password:> ")
        validate_password(password)
        pass_2 = getpass.getpass("password:> ")
        if password != pass_2:
            raise ValueError("Different password.")
        age = int(input("age:> "))
        self.hospital.register_user(username, password, age)

    def __make_function_dict(self):
        return {
                1: self.__login,
                2: self.__register,
                3: self.__start_menu,
                4: self.__exit}

    def __start_menu(self):
        print_help_menu()

    def __exit(self):
        sys.exit()
