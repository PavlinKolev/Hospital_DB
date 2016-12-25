import os
from user import User
from helper_prints import print_start_menu, print_doctor_options
from settings import DOCTOR_COMMANDS_COUNT
from validations import (validate_academic_title,
                        validate_doctor_username,
                        validate_age)


class Doctor(User):
    def __init__(self, username, age, id_, accademic_title):
        User.__init__(self, username, age, id_)
        self.accademic_title = accademic_title
        self.commands = self.__make_function_dict()

    def run_interface(self, hospital):
        while self.logged:
            os.system('clear')
            self.__start_menu(hospital)
            try:
                command = int(input("command:> "))
                self.__execute_command(command, hospital)
            except ValueError:
                input("Wrong input: No such command for doctor.\n" +
                        "Press Enter to continue...")

    def __execute_command(self, command, hospital):
        try:
            if command in range(DOCTOR_COMMANDS_COUNT):
                self.commands[command](hospital)
                if self.logged is False:
                    return
            else:
                print("Wrong input: No such command for doctor.")
        except ValueError as err:
            print("Wrong input: ", err)
        input("Press Enter to continue...")

    def __start_menu(self, hospital):
        print_start_menu(self.username, self.accademic_title)
        print_doctor_options()

    def __update_username(self, hospital):
        new_username = input("new username:> ")
        validate_doctor_username(new_username)
        hospital.update_user_username(self.id, new_username)
        self.username = new_username

    def __list_patients(self, hospital):
        hospital.all_patients_by_doctor(self.id)

    def __add_hour_for_visitation(self, hospital):
        start_hour = input("hour:> ")
        hospital.add_visitation(self.id, start_hour)

    def __delete_free_visitations(self, hospital):
        hospital.delete_free_visitations_of_doctor(self.id)

    def __list_room_and_hs_durations_of_patients(self, hospital):
        hospital.list_room_and_hs_durations_of_patients(self.id)

    def __options(self, hospital):
        print_doctor_options()

    def __make_function_dict(self):
        return {
                0: self.__options,
                1: self.__list_patients,
                2: self.__add_hour_for_visitation,
                3: self.__delete_free_visitations,
                4: self.__list_room_and_hs_durations_of_patients,
                5: self.__update_username,
                6: self.update_age,
                7: self.logout}
