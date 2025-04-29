myset = {"a", "b", "c", "d", "e", "f", "g"}
myset2 = {"b", "c", "d", "e", "f"}

if myset.issubset(myset2):
    print("myset myset2'ning quyi to'plami")
elif myset.issuperset(myset2):
    print("myset myset2'ning ustun to'plami")
else:
    print("Kesishma yo'q")