mylist = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for i in range(len(mylist)):
    if i % 2 != 0:
        print(mylist[i])
    else:
        continue