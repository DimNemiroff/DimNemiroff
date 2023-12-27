class User:
    login = "Guest"

    def greet(self):
        return print(f'Hi, my login is {self.login}')


class AuthenticatedUser(User):
    def __init__(self) -> None:
        super().__init__()


if __name__ == '__main__':
    alice = User()
    alice.greet()  # Hi, my login is Guest

    bob = User()
    bob.login = "Bob"
    bob.greet()  # Hi, my login is Bob
