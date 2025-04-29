mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

juft = []
toq = []

for i in mylist:
    if i % 2 == 0:
        juft.append(i)
    else:
        toq.append(i)
else:
    print(f"juftlar: {juft}\ntoqlar: {toq}")