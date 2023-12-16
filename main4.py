class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return "Meow"


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return "Woof"


cat = Cat("Simon", 10, "malaga")
dog = Dog("Barbos", 23, "labrador")
print(f'{cat.nickname} say {cat.say()}, but {dog.breed} {dog.nickname} the bigger than cat and say loudly {dog.say()} ')

