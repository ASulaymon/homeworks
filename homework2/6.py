vowel = [
    "a", "e", "i", "o", "u", "o'"
]

while True:
    word = str(input("So'z kiriting: "))
    if word == "stop":
        break
    else:
        for l in word:
            if l.lower() in vowel:
                print(l)
            else:
                continue
