def max_list(num_list):
    x = num_list[0]
    for i in num_list:
        if i > x:
            x = i
            return x


num_list = [20, 18, 89, 39, 72]
print('Maximum number is: ', max_list(num_list))

##


def max_num(x):
    max_value = x[0]
    for i in x:
        if i > max_value:
            max_value = i
    return max_value

def min_num(x):
    min_value = x[0]
    for i in x:
        if i < min_value:
            min_value = i
    return min_value


my_list = [9, 12, 32, 53, 72, 51, 61, 41]
print("Maximum number of the list: ", max_num(my_list))
print("Minimum number of the list: ", min_num(my_list))
