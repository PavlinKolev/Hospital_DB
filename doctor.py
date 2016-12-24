from prettytable import PrettyTable
from user import User
from validations import validate_academic_title, validate_doctor_username, validate_age
from helper_prints import print_choose_academic_title


def print_patients_after_query(patients):
    table = PrettyTable()
    table.field_names = ["ID", "Username", "Age"]
    for p in patients:
        table.add_row(p)
    print(table)


class Doctor(User):
    def __init__(self, username, password, age, gender, id_):
        User.__init__(self, username, password, age, gender, id_)
        self.accademic_title = None

    def set_accademic_title(self):
        print_choose_academic_title()
        title = input("accademic title:> ")
        validate_academic_title(academic_title)
        self.academic_title = academic_title

    def update_db_with_me(self, db, cursor):
        User.update_db_with_me(self, db, cursor)
        cursor.execute(ADD_DOCTOR, (self.id, self.academic_title))
        db.commit()

    def list_patients(self, cursor):
        cursor.execute(LIST_PATIENTS_OF_DOCTOR, (self.id))
        print_patients_after_query(cursor.fetchall())

    def add_hour_for_visitation(self, db, cursor):
        hour = input("hour:> ")
        cursor.execute(ADD_VISITATION, (None, self.id, hour))
        db.commit()

    def delete_free_visitations(self, db, cursor):
        cursor.execute(DELETE_FREE_VISITATIONS_OF_DOCTOR, (self.id, ))
        db.commit()

    def list_room_and_hs_durations_of_patients(self, cursor):
        cursor.execute(ROOM_AND_HS_DURATION_OF_DOCTOR_PATIENTS, (self.id, ))
        patients_hs = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["Username", "Room", "Startdate", "Enddate"]
        for p in patients_hs:
            table.add_row(p)
        print(table)

    def change_username(self, db, cursor):
        new_username = input("new username:> ")
        validate_doctor_username(new_username)
        cursor.execute(UPDATE_USER_USERNAME, (new_username, self.id))
        db.commit()

    def change_age(self, db, cursor):
        new_age = input("age:> ")
        validate_age(new_age)
        cursor.execute(UPDATE_USER_AGE, (new_age, self.id))
        db.commit()
