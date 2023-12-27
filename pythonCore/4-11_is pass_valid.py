import re

# import string


passwords = ('afdgd', 'KhnhfT568', 'asER56Vf', 'asdg246', 'qregqSGS', '')


def is_valid_password(str_for_valid: str) -> bool:
    valid = (len(str_for_valid) == 8,
             re.search('[A-Z]', str_for_valid),
             re.search('[a-z]', str_for_valid),
             re.search(r'\d', str_for_valid)
             )
    return all(valid)


for i in passwords:
    print(f'passwd {i} is {is_valid_password(i)}')
