# List = []
# n = int(input('Enter number of elements in list: '))
# for x in range(1, n + 1):
#     m = int(input('Enter the element: '))
#     List.append(m)
#
# print('Minimum number is: ', min(List))
#
# ##
#
#
# def small(list2):
#     a = list2[0]
#     for i in list2:
#         if i < a:
#             a = i
#     return a
#
#
# list2 = [19, 23, 12, 42, 71]
# print(small(list2))

##

list1 = []


class MinList:
    def __init__(self, list_size):
        self.list_size = list_size

    def getuser_inp(self):
        for i in range(self.list_size):
            a = int(input('Enter the element: '))
            list1.append(a)

    def min_num(self):
        min_val = list1[0]
        for i in range(self.list_size):
            if i == self.list_size - 1:
                return min_val
            y = list1[i + 1]
            if min_val > y:
                min_val = y
        return min_val


def main():
    list_size = int(input('Enter the number of element in the list: '))
    list_obj = MinList(list_size)
    list_obj.getuser_inp()
    print('Minimum number of list is: ', list_obj.min_num())


if __name__ == '__main__':
    main()



