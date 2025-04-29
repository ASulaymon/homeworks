mylist = ["a", "b", "c", "b", "a"]

newlist = []

for i in mylist:
    num = mylist.count(i)
    if num <= 1:
        newlist.append(i)
    else:
        continue
print(newlist)