myList = ["Badiiy", "Ilmiy-fantastik", "Ertak", "Fantastik", "Hikoya", "Roman", "Falklor"]

print(f"Siz o'qiydigan kitob turlari {str(myList)}")

while True:
    error = str(input("Noto'g'ri ko'rsatilgan janr bormi?\n>>"))

    if error.lower() == "yo'q":
        break
    else:
        if myList.__contains__(error.capitalize()):
            myList.remove(error.capitalize())
            print(myList)
            continue
        else:
            print("Bunday janr ro'yxatda yo'q")
            continue
