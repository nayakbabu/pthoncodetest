list2 = [10, 11, 12, 13, 14, 23, 34, 56, 29, 46, 51]
even_count = 0
odd_count = 0
num = 0
while(num < len(list2)):
    if list2[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num += 1
print('Total even numbers in the list: ', even_count)
print('Total odd numbers in the list: ', odd_count)

# ##
num = [12, 34, 13, 55, 67, 91, 63, 10]
for i in num:
    if(i % 2) == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')

##


class EvenOdd:
    def check_even_odd(self, num):
        if num % 2 == 0:
            return 1


print('Enter a number: ', end='')
num1 = int(input())

obj = EvenOdd()
check = obj.check_even_odd(num1)
if check == 1:
    print('Even Number')
else:
    print('Odd Number')