list1 = []


class MaxList:
    def __init__(self, num):
        self.num = num

    def max_num(self):
        x = list[0]
        for i in self.num:
            if i > x:
                x = i
                return x


def main():
    n = int(input('Enter the number of element in the list: '))
    m = MaxList(n)
    for i in range(n):
        a = int(input('Enter the element: '))
        list1.append(a)
    print('Maximum list is: ', max(list1))


if __name__ == "__main__":
    main()



