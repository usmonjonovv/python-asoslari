import random as r
tasodifiy_son1 = int(input('Endi sizni birorta son tanlang men topishga xarakat qilaman.\n- '))
def sontop_l(x=10):
    taxmin = r.randint(1,x)
    print(f"Menimcha javob:{taxmin}")
    savol = input('Javob taxmindan kichikroq bo\'lsa (-),katta(+),javob to\'g\'ri bo\'lsa(T) ishorasini qo\'ying.')
    while True:
        if savol == '+':
            taxmin +=1
            print(f"Menimcha javob:{taxmin}")
            savol = input('Javob taxmindan kichikroq bo\'lsa (-),katta(+),javob to\'g\'ri bo\'lsa(T) ishorasini qo\'ying.')
        elif savol == '-':
            taxmin -= 1
            print(f"Menimcha javob:{taxmin}")
            savol = input('Javob taxmindan kichikroq bo\'lsa (-),katta(+),javob to\'g\'ri bo\'lsa(T) ishorasini qo\'ying.')
        elif savol == 'T':
            print('O\'yin juda maroqli bo\'ldi rahmat!')
            break
print(sontop_l(10))