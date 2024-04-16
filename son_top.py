import random as r

def sontop1(x=10):
    tasodifiy_son = r.randint(1,x)
    print(f"Men 1 dan {x} gacha sonlarni o'yladim.Topa olsizmi?")
    flag = True
    while flag:
        taxmin = int(input('>>>'))
        if tasodifiy_son>taxmin:
            print('Men o\'ylagan son bundan kattaroq.Qaytadan urinib ko\'ring:')
        elif tasodifiy_son<taxmin:
            print('Men o\'ylagan son bundan kichikroq.Qaytadan urinib ko\'ring:')
        elif tasodifiy_son == taxmin:
            print('Tabriklaymiz topdingiz.')
            flag = False
print(sontop1(10))