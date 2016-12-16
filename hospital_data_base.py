import sqlite3
from prettytable import PrettyTable


class HospitalDB:
    DEFAULT_NAME = "hospital.db"

    def __init__(self, name=DEFAULT_NAME):
        self.name = name
        self.db = sqlite3.connect(name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.__create_doctors_table()
        self.__create_patients_table()
        self.__create_hospital_stay_table()
        self.patients_ids = []
        self.doctors_ids = []

    def __create_patients_table(self):
        self.cursor.execute(""" DROP TABLE IF EXISTS PATIENTS """)
        self.db.commit()
        create_patients_table = """
            CREATE TABLE IF NOT EXISTS PATIENTS
            (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                FIRSTNAME VARCHAR(255) NOT NULL,
                LASTNAME VARCHAR(255) NOT NULL,
                AGE INTEGER NOT NULL,
                GENDER CHAR(1) NOT NULL,
                DOCTOR_ID INTEGER,
                FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTORS(ID)
            )
        """
        self.cursor.execute(create_patients_table)
        self.db.commit()

    def __create_doctors_table(self):
        self.cursor.execute(""" DROP TABLE IF EXISTS DOCTORS """)
        self.db.commit()
        create_doctors_table = """
            CREATE TABLE IF NOT EXISTS DOCTORS
            (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                FIRSTNAME VARCHAR(255) NOT NULL,
                LASTNAME VARCHAR(255) NOT NULL
            )
        """
        self.cursor.execute(create_doctors_table)
        self.db.commit()

    def __create_hospital_stay_table(self):
        self.cursor.execute(""" DROP TABLE IF EXISTS HOSPITAL_STAYS """)
        self.db.commit()
        create_hospital_stays_table = """
            CREATE TABLE IF NOT EXISTS HOSPITAL_STAYS
            (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                START_DATE VARCHAR(255) NOT NULL,
                END_DATE VARCHAR(255),
                ROOM INTEGER NOT NULL,
                INJURY VARCHAR(255),
                PATIENT_ID INTEGER,
                FOREIGN KEY (PATIENT_ID) REFERENCES PATIENTS(ID)
            )
        """
        self.cursor.execute(create_hospital_stays_table)
        self.db.commit()

    def add_patient(self, first_name, last_name, age, gender, doctor_id):
        self.__validate_patient_data(age, gender, doctor_id)
        query = """
            INSERT INTO PATIENTS(FIRSTNAME, LASTNAME, AGE, GENDER, DOCTOR_ID)
            VALUES(?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (first_name, last_name, age, gender, doctor_id))
        self.patients_ids.append(self.cursor.lastrowid)
        self.db.commit()

    def add_doctor(self, first_name, last_name):
        query = """
            INSERT INTO DOCTORS(FIRSTNAME, LASTNAME)
            VALUES(?, ?)
        """
        self.cursor.execute(query, (first_name, last_name))
        self.doctors_ids.append(self.cursor.lastrowid)
        self.db.commit()

    def add_hospital_stay(self, start_date, room, patient_id, injury, end_date=None):
        self.__check_patient_id(patient_id)
        query = """
            INSERT INTO HOSPITAL_STAYS(START_DATE, END_DATE, ROOM, INJURY, PATIENT_ID)
            VALUES(?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (start_date, end_date, room, injury, patient_id))
        self.db.commit()

    def delete_patient(self, patient_id):
        self.__check_patient_id(patient_id)
        self.cursor.execute(""" DELETE FROM PATIENTS WHERE ID=?""", (patient_id,))
        self.db.commit()

    def delete_doctor(self, doctor_id):
        self.__check_doctor_id(doctor_id)
        self.cursor.execute(""" DELETE FROM DOCTORS WHERE ID=?""", (doctor_id,))
        self.db.commit()

    def delete_hospital_stay(self, hospital_stay_id):
        self.cursor.execute(""" DELETE FROM HOSPITAL_STAYS WHERE ID=?""", (hospital_stay_id,))
        self.db.commit()

    def list_all_patients(self):
        query = """
            SELECT ID, FIRSTNAME || " " || LASTNAME, AGE
            FROM PATIENTS
        """
        self.cursor.execute(query)
        patients = self.cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Id", "Name", "Age"]
        for p in patients:
            table.add_row([p[0], p[1], p[2]])
        print(table)

    def list_all_doctors(self):
        query = """
            SELECT ID, FIRSTNAME || " " || LASTNAME
            FROM DOCTORS
        """
        self.cursor.execute(query)
        doctors = self.cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Id", "Name"]
        for d in doctors:
            table.add_row([d[0], d[1]])
        print(table)

    def update_patient_first_name(self, patient_id, first_name):
        self.__check_patient_id(patient_id)
        query = """
            UPDATE PATIENTS
            SET FIRSTNAME=?
            WHERE ID=?
        """
        self.cursor.execute(query, (first_name, patient_id))
        self.db.commit()

    def update_patient_last_name(self, patient_id, last_name):
        self.__check_patient_id(patient_id)
        query = """
            UPDATE PATIENTS
            SET LASTNAME=?
            WHERE ID=?
        """
        self.cursor.execute(query, (last_name, patient_id))
        self.db.commit()

    def update_patient_age(self, patient_id, age):
        self.__check_patient_id(patient_id)
        self.__check_patient_age()
        query = """
            UPDATE PATIENTS
            SET AGE=?
            WHERE ID=?
        """
        self.cursor.execute(query, (age, patient_id))
        self.db.commit()

    def update_patient_doctors_id(self, patient_id, doctor_id):
        self.__check_patient_id(patient_id)
        self.__check_doctor_id(doctor_id)
        query = """
            UPDATE PATIENTS
            SET DOCTOR_ID=?
            WHERE ID=?
        """
        self.cursor.execute(query, (doctor_id, patient_id))
        self.db.commit()

    def update_doctor_first_name(self, doctor_id, first_name):
        self.__check_doctor_id(doctor_id)
        query = """
            UPDATE DOCTORS
            SET FIRSTNAME=?
            WHERE ID=?
        """
        self.cursor.execute(query, (first_name, doctor_id))
        self.db.commit()

    def update_doctor_last_name(self, doctor_id, last_name):
        self.__check_doctor_id(doctor_id)
        query = """
            UPDATE DOCTORS
            SET LASTNAME=?
            WHERE ID=?
        """
        self.cursor.execute(query, (last_name, doctor_id))
        self.db.commit()

    def __check_patient_id(self, patient_id):
        if patient_id not in self.patients_ids:
            raise ValueError("There is no patient with this ID.")

    def __validate_patient_data(self, age, gender, doctor_id):
        self.__check_patient_age(age)
        self.__check_patient_gender(gender)
        self.__check_doctor_id(doctor_id)

    def __check_patient_age(self, age):
        if type(age) is not int:
            raise TypeError("Type of patients age must be int.")
        if age < 0 or age > 120:
            raise ValueError("Not a valid patient age.")

    def __check_patient_gender(self, gender):
        if type(gender) is not str:
            raise TypeError("Type of gender must be string.")
        if gender != 'M' and gender != 'F':
            raise ValueError("Gender must be \'M\' or \'F\'.")

    def __check_doctor_id(self, doctor_id):
        if doctor_id not in self.doctors_ids:
            raise ValueError("There is no doctor with this id.")
