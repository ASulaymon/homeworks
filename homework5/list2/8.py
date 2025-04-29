mylist = ["Badiiy", "Ilmiy-fantastik", "Ertak", "Fantastik", "Hikoya", "Roman", "Falklor"]

while 1:
    janr = str(input(f"Qanday kitob janrini yoqtirasiz?\n>> "))
    
    if mylist.__contains__(janr):
        print(f"{janr} janridagi kitoblar allaqachon ro'yhatda bor!")
    else:
        mylist.append(janr)
        print(f"ro'yhatga qo'shildi!\nro'yxat: {mylist}")
