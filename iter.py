# tuple1 = (2, 5, 7, 9)
# iterator = iter(tuple1)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

##

# list1 = [2, 5, 13, 32, 52, 21, 41]
# iter1 = iter(list1)
# while True:
#     try:
#         print(next(iter1))
#     except StopIteration:
#         break

##

# class Iteration1:
#     def __init__(self, max=0):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:
#             result = self.n % 2
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#
#
# numbers = Iteration1(3)
# i = iter(numbers)
#
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

##

class InfIterator:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        result = self.n * 2
        self.n += 1
        return result


multi = InfIterator()
a = iter(multi)
print('Multiply of two are: ')
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))




