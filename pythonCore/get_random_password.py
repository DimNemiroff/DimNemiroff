from random import randint


def get_random_password():
    passwd = ""
    for i in range(length):
        passwd += chr(randint(A,B))
        print(passwd)
    return passwd


length = 8
A = 40
B = 126

'''()*+,-./:;<=>?@[\]^_`{|}~
48 - 57   0123456789
65 - 90   ABCDEFGHIJKLMNOPQRSTUVWXYZ
97 - 122  abcdefghijklmnopqrstuvwxyz
'''

get_random_password()
