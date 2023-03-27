class India:
    def capital(self):
        print('New Delhi is the capital of India')
    def lang(self):
        print('Hindi is the national language of India')
class Animal(India):
    def lang(self):
        print('Tiger is the national animal of India')
class Flower(India):
    def lang(self):
        print('Lotus is the national flower of India')

obj_1 = India()
obj_1.capital()
obj_1.lang()

obj_2 = Animal()
obj_2.capital()
obj_2.lang()

obj_3 = Flower()
obj_3.capital()
obj_3.lang()