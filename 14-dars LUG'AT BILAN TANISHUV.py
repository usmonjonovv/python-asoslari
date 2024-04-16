#1-mashq
oila = {'ota':'Ulug\'bek','t_yil':1986,'t_joy':'Oltinko\'l','ona':'Manzuraxon','t_yil1':1987,}
print(f"Otamning ismi {oila['ota']},u {oila['t_yil']}da {oila['t_joy']}da tug'ulgan.\nOnamning ismi {oila['ona']},u {oila['t_yil1']}da {oila['t_joy']}da tug'ulgan")
#2-mashq
fav_food = {'men':'kartoshka','muslimbek':'lavash','ona':'osh'}
print(f"Muslimbekning yoqtirgan ovqati {fav_food['muslimbek']}.\nOnamning yoqtirgan ovqati esa {fav_food['ona']}.")
#3-mashq
python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
kalit = input("Kalit so'z kiritng:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))
#4-mashq
if kalit == 'float' :
    print('FLoat o\'nlik son uni kop ishlatamiz hali bro!')
