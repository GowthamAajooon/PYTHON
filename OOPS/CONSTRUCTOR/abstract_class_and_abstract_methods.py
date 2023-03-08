from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class dog(Animal):
    def eat(self,food):
        self.food = food
        print(self.food)
        
c = dog()
c.eat("corn")


