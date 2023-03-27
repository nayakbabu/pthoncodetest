from abc import ABC, abstractmethod
class Human(ABC):
    @abstractmethod
    def speak(self):
        print('Human can speak')
class Animal(Human):
    def speak(self):
        super().speak()
        print('Animal can not speak')

x = Animal()
x.speak()
