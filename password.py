import hashlib


MIN_LENGTH = 8


def check_password(password):
    if len(password) <= MIN_LENGTH:
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


def encode(password):
    h = hashlib.sha512(password.encode())
    return h.hexdigest()
