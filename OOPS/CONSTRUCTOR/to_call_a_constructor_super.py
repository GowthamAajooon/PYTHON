class Animal:
    def __init__(self, name):
        self.name = name
        print("An animal is born.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A dog is born.")

dog = Dog("Fido")

An animal is born.
A dog is born.
