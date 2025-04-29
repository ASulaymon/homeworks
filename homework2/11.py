numbers = []

summ = 0

while True:
    num = int(input(">> "))

    if num == 0:
        break
    else:   
        numbers.append(num)
        summ += num
        length = numbers.__len__()
        mid_ad = summ / length
        print(mid_ad)
