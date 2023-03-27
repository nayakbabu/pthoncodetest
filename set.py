test_set = {1, 2, 3, 4, 5}
test_set1 = {9, 8, 7, 6}
test_set.update(test_set1)
print(test_set)
test_set2 = {10, 11, 12, 13, 14}
test_set3 = test_set1.union(test_set2)
print(test_set3)
test_set4 = test_set1.intersection(test_set2)