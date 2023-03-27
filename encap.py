class Emplo:
    def __init__(self):
        self.m = 'Ram'
        self.__m = 'Gita'
class Person(Emplo):
    def __init__(self):
        super().__init__()
        self.m = 'Sita'
        print(self.m)


about = Emplo()
print(about.m)
about2 = Person()
print(about2.m)