mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = 0


for i in range(len(mylist)):
    if i % 2 == 0:
        result += mylist[i]
    else:
        continue
else:
    print(result)
