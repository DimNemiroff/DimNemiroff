class User:
    login = "Guest"
    __mandatum = 10

    def __init__(self, login, mandatum):
        self.login = login
        self.__mandatum = mandatum

    def greet(self):
        print(f'Hi, my login is {self.login}')

    @property
    def mandatum(self):
        return self.__mandatum.name

    @mandatum.setter
    def mandatum(self, value):
        if hasattr(value, ) and self.__mandatum.level:
            self.__mandatum.name = value.name
            self.__mandatum.level = value.level

    def get_access(self, access_object):  # має поля name, level)

        if access_object.access_level < self.mandatum:
            print(access_object.name)
        else:
            print(f"Access to {access_object.name} denied!")

p = User(None, 0)
print(isinstance(p, User))
print(hasattr(p, "login"))


