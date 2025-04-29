mydict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

result = 0

for values in mydict.values():
    result += values
print(result)