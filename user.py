from password import check_password, encode


class User:
    def __init__(self, username, password, age, gender, id_):
        self.__set_username(username)
        self.__set_password(password)
        self.__set_gender(gender)
        self.__set_age(age)
        self.id = id_

    def __set_username(username):
        # Not white spaces
        self.username = username

    def __set_password(password):
        check_password(password)
        self.password = password

    def __set_age(age):
        if type(age) is not int:
            raise TypeError("Type of age must be int.")
        if age < 0 or age > 120:
            raise ValueError("Invalid age.")
        self.age = age

    def __set_gender(gender):
        if type(gender) is not str:
            raise TypeError("Gender must be string.")
        if gender!= 'M' and gender != 'F':
            raise ValueError("Gender must be \'M'\' or \'F\'")
        self.gender = gender
