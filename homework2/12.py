while True:
    word = str(input("So'z kiriting: "))
    if word == "stop":
        break
    else:
        for l in word:
            print(l)