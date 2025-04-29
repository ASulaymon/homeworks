n = int(input("son kiriting: "))
a = 1
result = 1


while True:
    if a <= n:
        result *= a
        a += 1
        print(result)