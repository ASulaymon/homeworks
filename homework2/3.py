while True:
    age = int(input("Yoshingiz nechada?\n>> "))

    if age < 18:
        print("Siz hali kichkinasiz!")
    elif age >= 18 and age <= 90:
        print("Voyaga yetgansiz!")
    else:
        print("Siz tuproqqa ko'proq yoting!")