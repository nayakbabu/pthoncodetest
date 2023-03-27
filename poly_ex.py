class Rabbit():
    def run(self):
        print('Rabbit run very fast')
    def speak(self):
        print('Rabbit can not speak')
class Tortoise():
    def run(self):
        print('Tortoise run very slow')
    def speak(self):
        print('It can not speak')

obj1 = Rabbit()
obj2 = Tortoise()

for animal in (obj1, obj2):
    animal.run()
    animal.speak()
