#1-mashq
ismlar = ['ali', 'vali', 'hasan', 'husan']
print("Salom " + ismlar[0].title() + ' bugun ko\'rishamizmi?')
print(ismlar[3].title() + ' qayerda ko\'rishamiz?')
#2-mashq
sonlar = [12, 14.4, -32]
#3-mashq
print(sonlar[0]+sonlar[-1])
print(sonlar[1]*sonlar[-2])
print(sonlar[1]/sonlar[0])
print(sonlar[0]+sonlar[2])
#4-mashq
sonlar.append('o\'n ikki')
sonlar.remove(12)
sonlar.insert(1, 15)
#5-mashq
t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")
#6-mashq
friends = []
friends.append('John')
friends.append('Alex')
friends.append('Danny')
friends.append('Sobirjon')
friends.append('Vanya')
print(friends)