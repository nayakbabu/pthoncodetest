class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name, self.id)
class Emp(Person):
    def __init__(self, name, id):
        self.name = name
        super().__init__(name, id)
    def print(self):
        print('Emp class')
Emp_details = Emp('Smruti', 23)
print(Emp_details.name, Emp_details.id)

##
class Movie:
    def movievar(self):
        print('Kick')
class City(Movie):
    def movievar(self):
        print('BBSR')
class Animal(Movie):
    def movievar(self):
        print('Dog')
class Fruits(City, Animal):
    def movievar(self):
        print('Apple')
obj = Fruits()
obj.movievar()
obj1 = City()
obj1.movievar()
obj2 = Animal()
obj2.movievar()
obj3 = Movie()
obj3.movievar()

