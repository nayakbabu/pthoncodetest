a = 'good morning'
for x in a:
    if x == 'd':
        break
    print(x)

# continue
a = 'good morning'
for x in a:
    if x == 'd':
        continue
    print(x)
fruits = ['apple', 'banana', 'cherry', 'kiwi']
for x in fruits:
    if x == "cherry":
        continue
    print(x)