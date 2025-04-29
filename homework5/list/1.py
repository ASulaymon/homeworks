numbers = []

while True:
    num = int(input(">> "))

    if num == 0:
        print(numbers)
        break
    else:
        numbers.append(num)
        print(f"{num} ro'yxatga qo'shildi")

