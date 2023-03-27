class my_class:
    __private_var = 203
    def __pri_method(self):
        print('Hello, Good Morning')
    def in_class(self):
        print('Good Night')
        self.__pri_method()

x = my_class()
x.in_class()

##

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender
    def intro(self):
        return self.__gender

person1 = Person(name='Raj', age= 25, gender= 'Male')
print('Name of the person', person1.name)
print('Age of the person', person1.age)
print('Gender of the person', person1.intro())


