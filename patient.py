import os
import datetime as dt
from user import User
from settings import PATIENT_COMMANDS, PATIENT_COMMANDS_COUNT
from helper_prints import (print_start_menu,
                            print_patient_options,
                            print_choose_injuries)


class Patient(User):
    def __init__(self, username, age, id_, doctor_id):
        User.__init__(self, username, age, id_)
        self.doctor_id = doctor_id
        self.commands = self.__make_function_dict()

    def run_interface(self, hospital):
        while self.logged:
            os.system('clear')
            self.__start_menu(hospital)
            try:
                command = int(input("command:> "))
                self.__execute_command(command, hospital)
            except ValueError:
                input("Wrong input: No such command for patient.\n" +
                        "Press Enter to continue...")

    def __execute_command(self, command, hospital):
        try:
            if command in range(PATIENT_COMMANDS_COUNT):
                self.commands[command](hospital)
                if self.logged is False:
                    return
            else:
                print("Wrong input: No such command for patient.")
        except ValueError as err:
            print("Wrong input: ", err)
        input("Press Enter to continue...")

    def __start_menu(self, hospital):
        print_start_menu(self.username, "patient")
        print_patient_options()

    def __update_doctor(self, hospital):
        print("Choose which doctor...")
        hospital.list_all_doctors()
        doctor_id = int(input("Doctor ID:> "))
        hospital.update_patient_doctors_id(self.id, doctor_id)
        self.doctor_id = doctor_id

    def __see_free_doctor_hours(self, hospital):
        hospital.list_free_visitations_of_doctor(self.doctor_id)

    def __reserve_hour_for_visit(self, hospital):
        print("Choose visitation id... ")
        hospital.list_free_visitations_of_doctor(self.doctor_id)
        visitation_id = int(input("visitation id:> "))
        hospital.update_visitation_patient_id(visitation_id, self.id)

    def __add_hospital_stay(self, hospital):
        print_choose_injuries()
        injury = input("injury:> ")
        days = int(input("For how many days from today?\n:> "))
        if days < 1:
            raise ValueError("Unvalid count of hospital stay\'s days.")
        start_date = dt.date.today()
        end_date = dt.date.today() + dt.timedelta(days=days)
        hospital.add_hospital_stay(start_date, 100, self.id, injury, end_date)

    def __print_doctor_accademic_title(self, hospital):
        print(hospital.get_accademic_title_of_doctor(self.doctor_id))

    def __list_hospital_stays(self, hospital):
        hospital.list_hs_of_patient(self.id)

    def __make_function_dict(self):
        return {
            0: self.__start_menu,
            1: self.__see_free_doctor_hours,
            2: self.__reserve_hour_for_visit,
            3: self.__add_hospital_stay,
            4: self.__print_doctor_accademic_title,
            5: self.__list_hospital_stays,
            6: self.__update_doctor,
            7: self.update_username,
            8: self.update_age,
            9: self.logout}
