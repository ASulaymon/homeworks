mylist = []

num = int(input("ro'yxata nichcha element qo'shjoq bo'songiz yozing\n>> "))
 
for i in range(0, num):
    e = int(input())

    mylist.append(e)
else:
    print(sorted(mylist))