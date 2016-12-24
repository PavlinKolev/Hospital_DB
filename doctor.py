from user import User
from hospital_data_base import HospitalDB
from validations import (validate_academic_title,
                        validate_doctor_username,
                        validate_age)


class Doctor(User):
    def __init__(self, username, password, age, gender, id_, accademic_title):
        User.__init__(self, username, password, age, gender, id_)
        self.accademic_title = accademic_title

    def update_username(self, hospital):
        new_username = input("new username:> ")
        validate_doctor_username(new_username)
        hospital.update_user_username(self.id, new_username)

    def update_age(self, hospital):
        new_age = input("age:> ")
        hospital.update_user_age(self.id, new_age)

    def update_accademic_title(self, hospital):
        print_choose_academic_title()
        accademic_title = input("accademic title:> ")
        hospital.update_doctor_academic_title(self.id, accademic_title)

    def list_patients(self, hospital):
        hospital.all_patients_by_doctor(self.id)

    def add_hour_for_visitation(self, hospital):
        start_hour = input("hour:> ")
        hospital.add_visitation(self.id, start_hour)

    def delete_free_visitations(self, db, cursor):
        hospital.delete_free_visitations_of_doctor(self.id)

    def list_room_and_hs_durations_of_patients(self, hospital):
        hospital.list_room_and_hs_durations_of_patients(self.id)

    def logout(self, hospital):
        hospital.user_logout(self.id)
