class Animal:
    def __init__(self, name):
        self.name = name
        print("An animal is born.")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print("A dog is born.")

dog = Dog("Fido")
