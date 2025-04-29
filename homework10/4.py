myset = {"a", "b", "s", "m", "d"}
myset2 = {"b", "c", "d", "e", "f"}
myset3 = {"d", "f", "b", "h", "i"}
union = myset3.union(myset.union(myset))
intersection = myset3.intersection(myset.intersection(myset2))

print(f"""
setlarning birlashmasi: {union}\n
setlarning kesishmasi: {intersection}
""")