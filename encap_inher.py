class Base:
    def __init__(self):
        self.x = 'Ram'
        self.__x = 25
class Div_clr(Base):
    def __init__(self):
        Base.__init__(self)
        self.x = 'XYZ'
        print(self.x)


obj1 = Base()
print(obj1.x)
obj2 = Div_clr()
print(obj1.x)

##

class Encap():
    def __init__(self):
        self._m = 50
class Inher(Encap):
    def __init__(self):
        Encap.__init__(self)
        print('Heloo', self._m)
        self._m = 23
        print('The num is: ', self._m)

x = Inher()
y = Encap()
print('First num is: ', x._m)
print('Second num is: ', y._m)

