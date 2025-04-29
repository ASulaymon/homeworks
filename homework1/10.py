result = 0

while True:
    num = int(input(">> "))

    if num > 0:
        result += num
    elif num < 0:
        continue
    else:
        print(result)
        break