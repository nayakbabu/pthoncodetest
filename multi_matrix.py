m = [[5, 6, 7],
     [2, 3, 4],
     [1, 8, 9]]
n = [[11, 12, 13],
     [14, 15, 16],
     [20, 21, 22]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for x in range(len(m)):
     for y in range(len(n)):
          result[x][y] = m[x][y] * n[x][y]
print(result)