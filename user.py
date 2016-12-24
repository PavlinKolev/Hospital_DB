from password import encode


class User:
    def __init__(self, username, password, age, gender, id_):
        self.__set_username(username)
        self.__set_password(password)
        self.__set_age(age)
        self.id = id_

    def __str__(self):
        return "{} - {} - {}".format(self.username, self.gender, self.password)

    def __repr__(self):
        return self.__str__()

    def __set_username(username):
        validate_username(username)
        self.username = username

    def __set_password(password):
        validate_password(password)
        self.password = encode(password)

    def __set_age(age):
        validate_age(age)
        self.age = age

    def update_db_with_me(self, db, cursor):
        cursor.execute(ADD_USER, (self.username, self.password, self.age))
        db.commit()
