a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
for x in a:
     print(x)
     for y in x:
          print(y)
b = 2
print(a * b)

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]]
n = [[2],
     [2],
     [2]]
for x in range(len(m)):
     for y in range(len(n)):
          print(n[y])