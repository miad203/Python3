import string
import secrets


def contains_upper(password: str):
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symble(password: str):
    for char in password:
        if char in string.punctuation:
            return True
    return False


def contains_digit(password):
    number = [x for x in password if x in string.digits]
    if any(number):
        return True
    return False


def generate_password(length: int, number: bool, symbols: bool, uppercase: bool):
    combination: str = string.ascii_lowercase + string.digits

    if uppercase:
        combination += string.ascii_uppercase
    if symbols:
        combination += string.punctuation
    if number:
        combination += string.digits

    combination_length: int = len(combination)
    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


if __name__ == '__main__':
    psk: str = generate_password(
        length=8, number=True, uppercase=True, symbols=False)
    print('password:', psk)
