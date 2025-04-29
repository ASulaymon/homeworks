words = []
while True:
    word = str(input("So'z kiriting: "))
    if word == "exit":
        break
    else:
        for l in word:
            words.append(l)
            length = words.index(l)
            length -= 1

            if length == 0:
                break
            else:
                print(words)
exit()

