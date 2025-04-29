biggest = None

while True:
    number = int(input(">> "))

    if number == 0:
        break
    elif biggest is None or number > biggest:
        biggest = number

        print(f"Kiritilgan eng katta son: {biggest}")
    else:
        print(f"Kiritilgan eng katta son: {biggest}")