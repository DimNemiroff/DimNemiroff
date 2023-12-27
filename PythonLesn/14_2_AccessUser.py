class User:
    __mandatum = 0

    def __init__(self, login, mandatum):
        self.login = login
        self.__mandatum = mandatum

    def greet(self):
        print(f'Hi, my login is {self.login}')
'''
    @property
    def mandatum(self):
        self.mandatum = mandatum
        return  
        
        
    @mandatum.setter
    def mandatum(self, user_level=None):
        self.mandatum = user_level
'''

    def get_access(self, access_object):  # має поля name, level)

        if access_object.access_level < self.mandatum:
            print(access_object.name)
        else:
            print(f"Access to {access_object.name} denied!")


class AccessLevel:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

    def __gt__(self, other):
        return self.level > other.level


class AccessObject:
    def __init__(self, _name, _content, _access_level):
        self.name = _name
        self.content = _content
        self.access_level = _access_level


if __name__ == '__main__':
    unclassified = AccessLevel("Unclassified", 1)
    secret = AccessLevel("Secret", 2)
    top_secret = AccessLevel("Top Secret", 3)

    alice = User("Alice", top_secret)
    bob = User("Bob", unclassified)

    password_database = AccessObject(
        "Password Database",
        "Alice - C00peR, Bob - uNc1e",
        secret
    )

    alice.greet()  # Hi, my login is Alice
    alice.get_access(password_database)  # Alice - C00peR, Bob - uNc1e

    bob.greet()  # Hi, my login is Bob
    bob.get_access(password_database)  # Access to Password Database denied!
