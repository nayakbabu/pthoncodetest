# def swap_num(list, a1, b1):
#     list[a1], list[b1] = list[b1], list[a1]
#     return list
#
#
# List = [20, 25, 18, 39, 52, 41]
# a1, b1 = 2, 5
# print(swap_num(List, a1-1, b1-1))
#
# ##
#
# swap_list = []
# x = int(input('Enter the number of elements: '))
# for x in range(0, x):
#     n = int(input('Enter the element: '))
#     swap_list.append(n)
# print('Enter the index')
# a = int(input('index1: '))
# b = int(input('index2: '))
#
# print('List is: ', swap_list)
# swap_list[a], swap_list[b] = swap_list[b], swap_list[a]
# print('After swapping: ', swap_list)

##

swapList2 = []

class SwapList:
    def __init__(self, list_size):
        self.list_size = list_size

    def getuser_inp(self):
        for i in range(self.list_size):
            b = int(input('Enter the element: '))
            swapList2.append(b)

    def swap_num(self):
        print('Enter the index')
        x1 = int(input('index1: '))
        y1 = int(input('index2: '))
        print('List is: ', swapList2)
        swapList2[x1], swapList2[y1] = swapList2[y1], swapList2[x1]
        return swapList2


def main():
    list_size = int(input('Enter the number of elements: '))
    list_obj = SwapList(list_size)
    list_obj.getuser_inp()
    print('After Swapping the list: ', list_obj.swap_num())


if __name__ == '__main__':
    main()




