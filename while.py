i = 1
while i < 10:
    i += 1
    if i == 7:
        continue
    print(i)
# List
a = [1, 2, 3, 4]
while a:
    print(a.pop())
##
x = 'good morning'
i = 0
while i < len(x):
    i += 1
    pass
print('value of i: ', i)
##
count = 0
while count < 5:
    print(count, "is less than 5")
    count = count + 1
else:
    print(count, "is not less than 5")