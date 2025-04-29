from math import *

mylist = [4, 5, 2, 8, 5, 8, 9]

length = len(mylist)
som = 0

for i in mylist:
    som += i
    result = som/length
else:
    print(f"taqriban {floor(result)}\nasl qiymat:{result}")