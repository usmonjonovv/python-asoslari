#1-mashq
shaxs1 = {'ismi':'Abdulhamid II',
          't_yil':1876,
          't_joy':'turkiya',
          'umr':42
          }
shaxs2 = {'ismi':'a.navoiy',
          't_yil':1441,
          't_joy':'xirot',
          'umr':60
          }
shaxs3 = {'ismi':'erkin vohidov',
          't_yil':1936,
          't_joy':'farg\'ona',
          'umr':80
          }
shaxslar = [shaxs1,shaxs2,shaxs3]
    
for shaxs in shaxslar:
    print(f"{shaxs['ismi'].title()}, "
          f"{shaxs['t_yil']}-yilda, "
          f"{shaxs['t_joy']}da tavallud topgan,va "
          f"{shaxs['umr']}-yil umr kechirgan.")
#2-mashq
asarlar = {
    'a.navoiy' : ['Hayrat ul-abror','Farhod va Shirin','Layli va Majnun','Sabʼai sayyor'],
    'abdulla qodiriy' : ['Kalvak Mahzumning xotira daftaridan','Toshpoʻlat tajang nima deydir?'],
    }
for yozuvchi,asar in asarlar.items():
    print(f'{yozuvchi.title()} quyidagi asarlar muallifi:')
    for asar1 in asar:
        print(asar1.title())
#3-mashq
dostlarim = {
    'izzatillo':['ingliz tili','matematika'],
    'asliddin':['matemtika','it'],
    'begmurod':['matematika','koresys tili'],
    'faxriyor':['ingliz tili','tarix'],
    }
for inson,fan in dostlarim.items():
    print(f'{inson.title()} quyidagi fanlarni o\'qiydi:')
    for f in fan:
        if f=='it':
            print(f.upper())
        else:
            print(f.title())
#3-mashq
davlatlar = {
    'india':{'capital':'mumbai',
             'area':2973190,
             'population':1145578
             },
    'china':{'capital':'shangai',
             'area':9388211,
             'population':4144151
             },
    'united states':{'capital':'washington',
                     'area':9147420,
                     'population':5154154
                     }
    }
for country,info in davlatlar.items():
    print(f"\n{country.title()}:\n"
          f"Area-{info['area']}.\n"
          f"Population-{info['population']}.")
#4-mashq
davlatlar = {
    'india':{'poytaxt':'mumbai',
             'area':2973,
             'aholi':11_000_000
             },
    'china':{'poytaxt':'shangai',
             'area':93882,
             'aholi':31_000
             },
    'united states':{'poytaxt':'washington',
                     'area':9147,
                     'aholi':18_000
                     }
    }
davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['area']} kv.km"
          f"\nAholisi: {info['aholi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")