#1-mashq
ism = input('Ismingizni kiriting:')
kitoblar = f"{ism.title()} yoqtirgan itoblaringizni kiriting:"
savol = ' '
while True:
    savol = input(kitoblar)
    if savol == 'stop':
        break
print('Rahmat')
#2-mashq
question = 'Enter your age:'

while True:
    age1 = input(question)
    if age1 == 'quit' or age1 == 'exit':
        break
    age = int(age1)
    

    if age>7:
        narh = 2
    elif 7<=age<18:
        narh = 3
    elif 18<=age<65:
        narh = 10
    else: narh = 0
    
    
    if narh == 0:
        print('It is free to you to enter to the zoo!')
    else: 
        print(f"Price of ticket is {narh} US dollars!")
#3-mashq
#berilgan dastur
#savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:
#    qiymat = input(savol)
#    if qiymat<0:
#        continue
#    elif qiymat=='Exit':
#        break
#    else:
#        ildiz = float(qiymat)**(0.5)
#        print(f"{qiymat} ning ildizi {ildiz} ga teng")
#to'g'irlangan dastur
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'quit' or qiymat == 'exit':
        break
    son = int(qiymat)
    if son<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(son)**(0.5)