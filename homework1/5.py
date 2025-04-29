result = 0

while True:
    num = int(input(">> "))

    if num != 0:
        result += num
    else:
        print(result)
        break