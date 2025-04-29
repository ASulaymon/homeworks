mytuple = ("a", "b", "c", "d")

mylist = list(mytuple)

mylist.append("e")

mytuple = tuple(mylist)

print(mytuple)