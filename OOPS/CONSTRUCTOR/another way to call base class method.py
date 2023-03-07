class Animal:
    def make_sound(self):
        print("An animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        Animal.make_sound(self)
        print("A dog barks.")

dog = Dog()
dog.make_sound()


An animal makes a sound.
A dog barks.
