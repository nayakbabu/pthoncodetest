x = [[2, 4, 6],
     [3, 5, 7],
     [9, 10, 11]]
y = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
add = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(y)):
        add[i][j] = x[i][j] + y[i][j]
print(add)



