class Employee:
     id = 10
     name = 'Smruti'
     def display(self):
         print(self.id, self.name)
emp = Employee()
emp.display()

##

class Person:
    def __init__(self, name, gender, profession):
        self.name = name
        self.gender = gender
        self.profession = profession
    def show(self):
        print('Name:', self.name, 'Gender:', self.gender, 'Profession:', self.profession)
    def work(self):
        print(self.name, 'working as a', self.profession)
about = Person('Nick', 'Male', 'Software Engineer')
about.show()
about.work()

##

class My_Intro:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Hello, my name is', self.name)
x = My_Intro('Smruti')
x.say_hello()