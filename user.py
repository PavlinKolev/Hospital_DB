from validations import validate_username


class User:
    def __init__(self, username, age, id_):
        self.username = username
        self.age = age
        self.id = id_
        self.logged = True

    def __str__(self):
        return "{} - {} - {}".format(self.username, self.gender, self.password)

    def __repr__(self):
        return self.__str__()

    def get_id(self):
        return self.id

    def update_username(self, hospital):
        new_username = input("new username:> ")
        validate_username(new_username)
        hospital.update_user_username(self.id, new_username)
        self.username = new_username

    def update_age(self, hospital):
        new_age = int(input("age:> "))
        hospital.update_user_age(self.id, new_age)
        self.age = new_age

    def logout(self, hospital):
        hospital.logout_user(self.id)
        self.logged = False
