class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def emply(self):
        return False
class Employee(Person):
    def emply(self):
        return True
emp = Person('Gita')
print(emp.getName(), emp.emply())
emp = Employee('Raj')
print(emp.getName(), emp.emply())