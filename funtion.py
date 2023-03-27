def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)
add_numbers(5, 4)

# Square
def square(num):
    result = num * num
    return result
x = square(8)
print("Square: ", x)

##
def outer_func():
    def inner_func():
        print("Hello, World!")
    inner_func()
outer_func()

##
def increment(number):
    def inner_increment():
        return number + 1
    return inner_increment()
print(increment(10))

##
def outer():
    x = 10
    def inner():
        print("Inside inner func", x)
    inner()
    print("Inside outer func", x)
outer()

##
def find_power(num):
    def power(n):
        return num ** n
    return power(2)
print(find_power(10))

##

def print_even(list):
    def find_even(num):
        if num % 2 == 0:
            return True
        else:
            return False
    new_list = []
    for num in list:
        if find_even(num) == True:
            new_list.append(num)
    print("Final list:", new_list)
mylist = [1, 2, 4, 5, 6, 7, 10, 11, 12, 14, 15, 16]
print_even(mylist)


