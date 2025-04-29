mylist = ["BMW", "Mercedes", "Peugeot", ["Nexia 2", "Cobalt", "Tico"]]
newlist = []

for i in mylist:
    if type(i) == list:
        for e in i:
            newlist.append(e)
    else:
        newlist.append(i)
else:
    print(newlist)