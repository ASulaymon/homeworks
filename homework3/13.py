unli = [
    "a",
    "e",
    "i",
    "o",
    "u",
    "o'"
]

word = str(input(">> "))

for i in word:
    if unli.__contains__(i):
        print(i)