from settings import INJURIES, ACADEMIC_TITLES


def validate_username(username):
    if type(username) is not str:
        raise TypeError("Type of username must be str.")


def validate_password(password):
    if len(password) <= 8  # MIN_LENGTH:
        raise ValueError("Length of password must be at least {} symbols".format(MIN_LENGTH))
    no_upper = True
    no_lower = True
    no_digit = True
    for letter in password:
        if letter.isupper():
            has_upper = False
        if letter.islower():
            has_lower = False
        if letter.isdigit():
            has_digit = False
    if no_upper:
        raise ValueError("Password must have capital letter.")
    if no_lower:
        raise ValueError("Password must have lower letter.")
    if no_digit:
        raise ValueError("Password must have digit.")


def validate_age(age):
    if type(age) is not int:
        raise TypeError("Type of age must be int.")
    if age < 0 or age > 120:
        raise ValueError("Invalid age.")


def validate_gender(gender):
    if type(gender) is not str:
        raise TypeError("Gender must be of type string.")
    if gender != 'M' and gender != 'F':
        raise ValueError("Gender can be \'M or \'F")


def valudate_injury(injury):
    if injury not in INJURIES:
        raise ValueError("Unrecognised injury.")


def validate_academic_title(academic_title):
    if academic_title not in ACADEMIC_TITLES:
        raise ValueError("Unrecognised academic title.")

def validate_doctor_username(username):
    if type(username) is not str or not(username.startswith("Dr.")):
        raise ValueError("A doctor username must start with \"Dr.\"")
