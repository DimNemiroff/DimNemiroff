from random import randint
import re


def get_random_password():
    passwd = ""
    for i in range(8):
        passwd += chr(randint(40, 126))
    return passwd


def is_valid_password(str_for_valid: str) -> bool:
    valid = (len(str_for_valid) == 8,
             re.search('[A-Z]', str_for_valid),
             re.search('[a-z]', str_for_valid),
             re.search(r'\d', str_for_valid)
             )
    return all(valid)


def get_password():
    for i in range(100):
        password = get_random_password()
        if is_valid_password(password):
            return password
        i += 1


print(get_password())
