class User:
    login = "Guest"

    def greet(self):
        return print(f'Hi, my login is {self.login}')


class AuthenticatedUser(User):
    def __init__(self, user_password):
        self.user_password = "password"

    def authenticate(self, user_password):
        return self.user_password == password


password = "password"

if __name__ == '__main__':
    alice = User()
    alice.greet()  # Hi, my login is Guest

    bob = User()
    bob.login = "Bob"
    bob.greet()  # Hi, my login is Bob

    alice = AuthenticatedUser(password)
    alice.greet()  # Hi, my login is Guest
    is_alice = alice.authenticate("password")
    print(f"Is 'alice' a default AuthenticatedUser: {is_alice}")  # Is 'alice' a default AuthenticatedUser: True

    bob = AuthenticatedUser(password)
    bob.login = "Bob"
    bob.user_password = "uNc1e"
    bob.greet()  # Hi, my login is Bob
    is_bob = bob.authenticate("password")
    print(f"Is 'bob' a default AuthenticatedUser: {is_bob}")  # Is 'bob' a default AuthenticatedUser: False
