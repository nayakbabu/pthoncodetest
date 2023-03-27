def add(num):
    return num + 4
print(add(6))

##

x = lambda a, b, c: a + b + c
print(x(5, 6, 7))

##

def my_function(n):
    return lambda a: a * n
fun1 = my_function(5)
fun2 = my_function(6)
print(fun1(10))
print(fun2(11))

##

minimum = lambda x, y: x if(x < y) else y
print(minimum(23, 34))

