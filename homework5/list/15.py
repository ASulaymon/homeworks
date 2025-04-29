mylist = ["Teacher", "Artist", "Coder", "Programmer", "Designer"]
mylist2 = ["Actor", "Engineer", " ", "Builder", "Designer"]

newlist = []

for i in mylist2:
    if i in mylist:
        newlist.append(i)
    else:
        continue
else:
    print(newlist)