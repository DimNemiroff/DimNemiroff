from PythonLesn.HW_12.main import User


class AuthenticatedUser(User):
    password = "password"

    def authenticate(self, password):
        return self.password == password


if __name__ == '__main__':
    alice = AuthenticatedUser()
    alice.greet()  # Hi, my login is Guest
    is_alice = alice.authenticate("password")
    print(f"Is 'alice' a default AuthenticatedUser: {is_alice}")  # Is 'alice' a default AuthenticatedUser: True

    bob = AuthenticatedUser()
    bob.login = "Bob"
    bob.password = "uNc1e"
    bob.greet()  # Hi, my login is Bob
    is_bob = bob.authenticate("password")
    print(f"Is 'bob' a default AuthenticatedUser: {is_bob}")  # Is 'bob' a default AuthenticatedUser: False
