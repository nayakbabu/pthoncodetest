from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print('I can run')
class Birds(Animal):
    def move(self):
        print('I can fly')
class Dog(Animal):
    def move(self):
        print('I can Bark')
class Fruits(Animal):
    def move(self):
        print('Mango is my favourite fruit')

x = Human()
x.move()

y = Birds()
y.move()

z = Dog()
z.move()

z1 = Fruits()
z1.move()
