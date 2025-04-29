mytuple = ("a", 2, 3, 5, 6, "b", 10, "c", 1, "d")

for i in mytuple:
    if str(i).isdigit() and int(i)%2 == 0:
        print(i)