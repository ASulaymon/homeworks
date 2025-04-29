mylist = ["Badiiy", "Ilmiy-fantastik", "Ertak", "Fantastik", "Hikoya", "Roman", "Falklor"]

newlist = []

newlist.insert(0, mylist.pop(len(mylist) - 1))
for i in mylist:
    newlist.append(i)

print(newlist)