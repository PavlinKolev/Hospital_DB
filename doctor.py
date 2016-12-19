from user import User


class Doctor(User):
    def __init__(self, username, password, age, gender, id_, academic_title):
        super.__init__(username, password, age, gender, id_)
        self.academic_title = academic_title
