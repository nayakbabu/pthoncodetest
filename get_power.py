def power(x, m):
    if m == 0:
        return 1
    elif m == 1:
        return x
    else:
        return (x * power (x, m-1))

x = 5
p = 2
print(power(x, p))

##

num = int(input("Enter any positive integer: "))
power = int(input("Enter the value: "))
s = 1
for i in range(1, power+1):
    s = s * num
print("The result of {0} Power {1} = {2}". format(num, power, s))

