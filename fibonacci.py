def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10)

##

num = int(input('Enter the range: '))
x = 0
y = 1
for i in range(0, num):
    if(i <= 1):
        m = i
    else:
        m = x + y
        x = y
        y = m
    print(m)

##

class TestWhile:
    def __init__(self, limit):
        self.limit = limit
    def fibonaci(self):
        x1 = x2 = sum = 0
        for i in range(0, self.limit):
            if i <= 1:
                x1 = i
                print(x1)
            else:
                sum = x1 + x2
                x2 = x1
                x1 = sum
                print(sum)

def main():
    max_limit = int(input('Enter the max limit: '))
    text_fib = TestWhile(max_limit)
    text_fib.fibonaci()
    text_fib1 = TestWhile(10)
    text_fib1.fibonaci()

if __name__ == "__main__":
    main()

