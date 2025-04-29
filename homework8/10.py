mytuple = ("a", 2, 6, "b", 10, "c", 1, "d")
result = 0

for i in mytuple:
    if str(i).isdigit():
        result += int(i)
print(result)