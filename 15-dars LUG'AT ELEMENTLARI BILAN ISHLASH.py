#1-mashq
dict = {'apple':'olma',
        'good morning':'ertalabki salom',
        'good night':'tungi salom',
        'float':'o\'nlik sonlar',
        'integer':'butun son'
        }
for k,q in dict.items():
    print(f'{k.title()}-{q.title()}')
#2-mashq
cc = {'usa':'washington DC',
      'bba':'sharm al sheikh',
      'uzbekistan':'tashkenet',
      'afganistan':'kobul',
      'korea':'seul'
      }
for a,b in cc.items():
    print(f'{a.title()} davlatning poytaxti - {b.title()}')
print('Davlatlar:')
for a in cc.keys():
    print(a.title())
print('Ularning poytaxtlari:')
for b in cc.values():
    print(b.title())
#3-mashq
cc1=input('Qaysi davlar poytaxtini bilmoqchisiz? \n-').lower()
capital=cc.get(cc1)
if capital==None:
    print('Bizda bunday ma\'lumot yo\'q')
else:
    print(f'{cc1.upper()}ning poytaxti {capital.title()}')
country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = cc.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
#4-mashq
menu = {'osh':10000,
        'somsa':6000,
        'norin':25000,
        'shashlik':12000,
        'nonkabob':18000,
        'shaurma':15000,
        'l_choy':5000,
        'lag\'mon':20000
        }
print('Buyurtmani kiriting:\n')
buyurtma=[]
for n in range(3):
    buyurtma.append(input(f"{n+1}-taom:").lower())
    
for taom in buyurtma:
    if taom in menu:
        print(f'{taom.title()} {menu[taom]} so\'m.')
    else:
        print('Bunday taom yo\'q!')
#for buyurtma in buyurtma:
#    if buyurtma in menu:
#        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#    else:
#        print(f"Kechirasiz, bizda {buyurtma} yo'q.")