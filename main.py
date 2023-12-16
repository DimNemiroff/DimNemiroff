class User:
    def __init__(self, login="Guest"):
        self.login = login

    def greet(self):
        print(f'Hi! My login is {self.login}')


if __name__ == '__main__':
    alice = User()
    alice.greet()  # Hi, my login is Guest

    bob = User()
    bob.login = "Bob"
    bob.greet()  # Hi, my login is Bob