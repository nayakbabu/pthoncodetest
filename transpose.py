a = [[12, 13, 14],
     [15, 16, 17],
     [18, 19, 11]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for x in range(len(a)):
     for y in range(len(a[0])):
          result[y][x] = a[x][y]

print(result)