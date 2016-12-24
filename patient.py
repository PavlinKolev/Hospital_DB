import datetime as dt
from user import User
from hospital_data_base import HospitalDB


class Patient(User):
    def __init__(self, username, password, age, gender, id_, doctor_id):
        User.__init__(self, username, password, age, gender, id_)
        self.doctor_id = doctor_id

    def update_username(self, hospital):
        new_username = input("new username:> ")
        hospital.update_user_username(self.id, new_username)

    def update_age(self, hospital):
        new_age = int(input("age:> "))
        hospital.update_user_age(self.id, new_age)

    def update_doctor(self, hospital):
        print("Choose which doctor...")
        hospital.list_all_doctors()
        doctor_id = int(input("Doctor ID:> "))
        hospital.update_patient_doctors_id(doctor_id)

    def see_free_doctor_hours(self, hospital):
        hospital.list_free_visitations_of_doctor(self.doctor_id)

    def reserve_hour_for_visit(self, hospital):
        print("Choose visitation id... ")
        hospital.list_free_visitations_of_doctor(self.doctor_id)
        visitation_id = int(input("visitation id:> "))
        hospital.update_visitation_patiet_id(self.id)

    def add_hospital_stay(self, hospital):
        print_choose_injuries()
        injury = input("injury:> ")
        days = int(input("For how many days from today?\n:> "))
        if days < 1:
            raise ValueError("Unvalid count of hospital stay\'s days.")
        start_date = dt.date.today()
        end_date = dt.date.today() - dt.timedelta(days=days)
        hospital.add_hospital_stay(start_date, 100, self.id, injury, end_date)

    def print_doctor_accademic_title(self, hospital):
        print(hospital.get_accademic_title_of_doctor(self.doctor_id))

    def list_hospital_stays(self, hospital):
        hospital.list_hs_of_patient(self.id)

    def logout(self, hospital):
        hospital.user_logout(self.id)
