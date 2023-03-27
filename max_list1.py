list1 = []


class MaxList:
    def __init__(self, list_size):
        self.list_size = list_size

    def get_user_inp(self):
        for i in range(self.list_size):
            a = int(input('Enter the element: '))
            list1.append(a)

    def max_num(self):
        if self.list_size == 0:
            return 0
        max_val = list1[0]
        for i in range(self.list_size):
            if i == self.list_size-1:
                return max_val
            y = list1[i + 1]
            if max_val < y:
                max_val = y
        return max_val


def main():
    list_size = int(input('Enter the number of element in the list: '))
    list_obj = MaxList(list_size)
    list_obj.get_user_inp()
    print('Maximum number of list is: ', list_obj.max_num())
    list_size1 = int(input('Enter the number of element in the list: '))
    list_obj = MaxList(list_size1)
    list_obj.get_user_inp()
    print('Maximum number of list is: ', list_obj.max_num())


if __name__ == '__main__':
    main()
