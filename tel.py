import re
andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
tel = input("Telefon raqamingizni kiriting: ")
matches = []
while True:
    if re.match(andoza,tel):
        matches.append(tel)
        print("Telefon raqamingiz qabul qilindi!")
        break
    else:
        print("Iltimos qaytadan (998) bilan kiriting: ")
