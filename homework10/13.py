myset = {1, 2, 3, 4, 5, 6}
newset = set()

for i in myset:
    if i % 2 == 0:
        newset.add(i)
print(newset)