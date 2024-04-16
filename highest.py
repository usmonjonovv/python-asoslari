def Kattasi(x,y,z):
    sonlar = [x,y,z]
    if x == max(sonlar):
        highest = x
    elif y == max(sonlar):
        highest = y
    elif z == max(sonlar):
        highest = z
    return f"Ro'yxatdagi eng katta son: {highest}"
print(Kattasi(4,5,2))