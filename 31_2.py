
class Talaba():
    __talaba_soni = 0
    def __init__(self,ism,familiya,passport,tyil,idraqam,bosqich):
        self.idraqam = idraqam
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__bosqich = bosqich
        self.fanlar = []
        Talaba.__talaba_soni += 1

    def update_bosqich(self,bosqich):
        if bosqich >= 0:
            self.__bosqich+= bosqich
            print(f'Bosqich yangilandi!Hozirgi bosqich {self.__bosqich}')
        else:
            print('Bosqichni kamaytirib bo\'lmaydi!')        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    def fan_yozil(self):
        self.fanlar.append(Fanlar)
        return self.fanlar
    
    def remove_fan(self):
        while True:
            remove1 = input('Olib tashlash uchun fanni kiriting: ')
            if remove1 in self.fanlar:
                self.fanlar.remove(remove1)
                print('Bu fan olib tashlandi.')
                another = input('Yana boshqa fanni olib tashlamoqchimisiz? (yes/no)')
                if another != 'yes':
                    break
            elif remove1 not in self.fanlar:
                print('Siz bu fanga yozilmagansiz!')
                break
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    @classmethod
    def get_talaba_soni(cls):
        return cls.__talaba_soni
    
class Fanlar():
    def __init__(self,n_subjects):
        self.n_subjects = n_subjects
        self.names = []

    def get_info_subjects(self):
        return f"Number of subjects:{self.n_subjects}\nList of subjects:{self.names}"

    def fanlar(self):
        while True:
            fan = input('O\'qiyotgan faningiz nomi kiriting: ')
            self.names.append(fan)
            yana = input('Yana fan kiritasizmi? (xa/yo\'q)')
            if yana != 'xa':
                break
    def get_info_matem(self):
        for f in self.names:
            print(f)
            info = f"Number of students:{self.s_number}\nNumber of lessons in a week:{self.in_week}"
            info += f"Tutor:{self.tutor.title()}"
        return info