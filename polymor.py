class Bird:
    def about(self):
        print('Many types of Birds')
    def fly(self):
        print('Birds can fly but some cannot')
    def eat(self):
        print('Birds can eat')
class Parrot(Bird):
    def fly(self):
        print('Parrot can fly')
    def eat(self):
        print('Parrot can eat')
class Ostrich(Bird):
    def fly(self):
        print('Ostrich cannot fly')
    def eat(self):
        print('Ostrict can eat')

obj = Bird()
obj.about()
obj.fly()
obj.eat()

obj1 = Parrot()
obj1.about()
obj1.fly()
obj1.eat()

obj2 = Ostrich()
obj2.about()
obj2.fly()
obj2.eat()