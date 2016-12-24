from user import User


class Patient(User):
    def __init__(self, username, password, age, gender, id_, doctor_id):
        User.__init__(self, username, password, age, gender, id_)
        self.doctor_id = doctor_id
