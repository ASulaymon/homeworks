my_tuple = (1, 2, 3, 2, 4, 5, 2)

nums = {x: my_tuple.count(x) for x in set(my_tuple) if my_tuple.count(x) > 1}

print("Takrorlangan sonlar:", nums)