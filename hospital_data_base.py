import sqlite3
from prettytable import PrettyTable
from queries import *
from settings import DEFAULT_HOSPITAL_NAME, ACADEMIC_TITLES, INJURIES
from validations import *
from password import encode


class HospitalDB:
    def __init__(self, name=DEFAULT_HOSPITAL_NAME):
        self.db = sqlite3.connect(name + '.db')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.__create_doctors_table()
        self.__create_patients_table()
        self.__create_hospital_stay_table()
        self.__create_visitation_table()
        self.set_users_ids()
        self.set_patients_ids()
        self.set_doctors_ids()
        self.set_hospital_ids()
        self.set_visitations_ids()

    def __del__(self):
        self.db.close()

    # we want to close the database even if not handled exeption occurs
    def __exit__(Self, exc_type, exc_value, traceback):
        self.db.close()

    def set_users_ids(self):
        self.cursor.execute(LIST_USER_IDS)
        users = self.cursor.fetchall()
        self.users_ids = [u["ID"] for u in users]

    def set_patients_ids(self):
        self.cursor.execute(LIST_PATIENT_IDS)
        patients = self.cursor.fetchall()
        self.patients_ids = [p["ID"] for p in patients]

    def set_doctors_ids(self):
        self.cursor.execute(LIST_DOCTOR_IDS)
        doctors = self.cursor.fetchall()
        self.doctors_ids = [d["ID"] for d in doctors]

    def set_hospital_ids(self):
        self.cursor.execute(LIST_HOSPITAL_STAY_IDS)
        hospital_stays = self.cursor.fetchall()
        self.hospital_stay_ids = [hs["ID"] for hs in hospital_stays]

    def set_visitations_ids(self):
        self.cursor.execute(LIST_VISITATION_IDS)
        visitations = self.cursor.fetchall()
        self.visitations_ids = [v["ID"] for v in visitations]

    def __create_user_table(self):
        self.cursor.execute(CREATE_USER_TABLE)
        self.db.commit()

    def __create_patients_table(self):
        self.cursor.execute(CREATE_PATIENT_TABLE)
        self.db.commit()

    def __create_doctors_table(self):
        self.cursor.execute(CREATE_DOCTOR_TABLE)
        self.db.commit()

    def __create_hospital_stay_table(self):
        self.cursor.execute(CREATE_HOSPITAL_STAY_TABLE)
        self.db.commit()

    def __create_visitation_table(self):
        self.cursor.execute(CREATE_VISITATION_TABLE)
        self.db.commit()

    def add_user(self, username, password, age):
        validate_username(username)
        validate_password(password)
        validate(age)
        self.cursor.execute(ADD_USER, (username, encode(password), age))
        self.db.commit()

    def add_patient(self, id_, doctor_id):
        self.__validate_user_id(id_)  # there is have to be user with this id
        self.__validate_doctor_id(doctor_id)  # same with the doctor
        self.cursor.execute(ADD_PATIENT, (id_, doctor_))
        self.db.commit()
        self.patients_ids.append(id_)

    def add_doctor(self, id_, academic_title):
        self.__validate_user_id(id_)
        validate_academic_title(academic_title)
        self.cursor.execute(ADD_DOCTOR, (id_, academic_title))
        self.db.commit()
        self.doctors_ids.append(id_)

    def add_hospital_stay(self, startdate, room, patient_id, injury, enddate=None):
        validate_injury(injury)
        self.__validate_patient_id(patient_id)
        self.cursor.execute(ADD_HOSPITAL_STAY,
                            (startdate, enddate, room, injury, patient_id))
        self.db.commit()
        self.hospital_stay_ids.append(self.cursor.lastrowid)

    def add_visitation(self, doctor_id, start_hour, patient_id=None):
        self.__validate_doctor_id(doctor_id)
        if patient_id:
            self.__validate_patient_id(patient_id)
        self.cursor.execute(ADD_VISITATION, (patient_id, doctor_id, start_hour))
        self.db.commit()

    def delete_user(self, user_id):
        self.__validate_user_id(user_id)
        self.cursor.execute(DELETE_USER, (user_id))
        self.db.commit()

    def delete_patient(self, patient_id):
        self.__validate_patient_id(patient_id)
        self.cursor.execute(DELETE_PATIENT, (patient_id,))
        self.db.commit()

    def delete_doctor(self, doctor_id):
        self.__validate_doctor_id(doctor_id)
        self.cursor.execute(DELETE_DOCTOR, (doctor_id,))
        self.db.commit()

    def delete_hospital_stay(self, hospital_stay_id):
        self.__validate_hs_id(hospital_stay_id)
        self.cursor.execute(DELETE_HOSPITAL_STAY, (hospital_stay_id,))
        self.db.commit()

    def delete_free_visitations_of_doctor(self, doctor_id):
        self.__validate_doctor_id(doctor_id)
        self.cursor.execute(DELETE_FREE_VISITATIONS_OF_DOCTOR, (doctor_id, ))
        self.db.commit()

    def get_accademic_title_of_doctor(self, doctor_id):
        self.__validate_doctor_id(doctor_id)
        self.cursor.execute(DOCTOR_ACCADEMIC_TITLE, (doctor_id, ))
        return self.cursor.fetchone()["ACCADEMIC_TITLE"]

    def list_all_patients(self):
        self.cursor.execute(LIST_ALL_PATIENTS)
        self.__print_patients_after_query()

    def list_all_doctors(self):
        self.cursor.execute(LIST_ALL_DOCTORS)
        doctors = self.cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Id", "Username", "Academic title"]
        for d in doctors:
            table.add_row(d)
        print(table)

    def list_free_visitations_of_doctor(self, doctor_id):
        self.__validate_doctor_id(doctor_id)
        self.cursor.execute(LIST_FREE_VISITATIONS_OF_DOCTOR, (doctor_id, ))
        visitations = self.cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Id", "Start hour"]
        for v in visitations:
            table.add_row(v)
        print(table)

    def list_room_and_hs_durations_of_patients(self, doctor_id):
        self.__validate_doctor_id(doctor_id)
        self.cursor.execute(ROOM_AND_HS_DURATION_OF_DOCTOR_PATIENTS,(doctor_id, ))
        patients_hs = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Username", "Room", "Startdate", "Enddate"]
        for p in patients_hs:
            table.add_row(p)
        print(table)

    def list_hs_of_patient(self, patient_id):
        self.__validate_patient_id(patient_id)
        self.cursor.execute(LIST_HS_FOR_PATIENT, (patient_id))
        hospital_stays = self.cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Startdate", "Enddate", "Room", "Injury"]
        for hs in hospital_stays:
            table.add_row(hs)
        print(table)

    def __print_patients_after_query(self):
        patients = self.cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["ID", "Username", "Age"]
        for p in patients:
            table.add_row(p)
        print(table)

    def is_user_logged_in(self, user_id):
        self.__validate_user_id(user_id)
        self.cursor.execute(USER_STATUS, (user_id, ))
        return (self.cursor.fetchone()["IS_ACTIVE"] != 0)

    def user_login(self, user_id):
        if self.is_user_logged_in(user_id):
            raise ValueError("This user is already logged in\
                                from another application.")
        self.cursor.execute(UPDATE_USER_IS_ACTIVE, (1, user_id))
        self.db.commit()

    def user_logout(self, user_id):
        self.__validate_user_id(user_id)
        self.cursor.execute(UPDATE_USER_IS_ACTIVE, (0, user_id))
        self.db.commit()

    def update_user_username(self, user_id, username):
        validate_username(username)
        self.__validate_user_id(user_id)
        self.cursor.execute(UPDATE_USER_USERNAME, (username, user_id))
        self.db.commit()

    def update_user_age(self, user_id, age):
        validate_age(age)
        self.__validate_user_id(user_id)
        self.cursor.execute(UPDATE_USER_AGE, (age, user_id))
        self.db.commit()

    def update_patient_doctors_id(self, patient_id, doctor_id):
        self.__validate_patient_id(patient_id)
        self.__validate_doctor_id(doctor_id)
        self.cursor.execute(UPDATE_PATIENT_DOCTOR_ID, (doctor_id, patient_id))
        self.db.commit()

    def update_doctor_academic_title(self, doctor_id, academic_title):
        validate_academic_title(academic_title)
        self.__validate_doctor_id(doctor_id)
        self.cursor.execute(UPDATE_DOCTOR_ACADEMIC_TITLE, (academic_title, doctor_id))
        self.db.commit()

    def update_visitation_patiet_id(self, visitation_id, patient_id):
        self.__validate_visitation_id(visitation_id)
        self.__validate_patient_id(patient_id)
        self.cursor.execute(UPDATE_VISITATION_PATIENT_ID, (patient_id, visitation_id))
        self.db.commit()

    def all_patients_by_doctor(self, doctor_id):
        self.__validate_doctor_id(doctor_id)
        self.cursor.execute(LIST_PATIENTS_OF_DOCTOR, (doctor_id,))
        self.__print_patients_after_query()

    def __validate_user_id(self, user_id):
        if user_id not in self.users_ids:
            raise ValueError("There is no user with this id.")

    def __validate_patient_id(self, patient_id):
        if patient_id not in self.patients_ids:
            raise ValueError("There is no patient with this ID.")

    def __validate_doctor_id(self, doctor_id):
        if doctor_id not in self.doctors_ids:
            raise ValueError("There is no doctor with this id.")

    def __validate_hs_id(self, hs_id):
        if hs_id not in self.hospital_stay_ids:
            raise ValueError("There is no hospidatl stay with this id.")

    def __validate_visitation_id(self, visitation_id):
        if visitation_id not in self.visitations_ids:
            raise ValueError("There is no visitation with this id.")
