class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Tutor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,n_lessons,w_years):
        super().__init__(ism, familiya, passport, tyil)
        self.n_lessons = n_lessons
        self.w_years = w_years
    def get_n_lessons(self):
        return self.n_lessons
    def get_wyears(self):
        return self.w_years
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Darslar soni:{self.n_lessons}\nIsh tajribasi:{self.w_years}"

class User(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,email,number):
        super().__init__(ism, familiya, passport, tyil)
        self.email = email
        self.number = number
    def get_email(self):
        return self.email
    def get_number(self):
        return self.number
    def get_all(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Foydalanuvchi elektron pochtasi: {self.email}"
        info += f"Foydalanuvchi raqami: {self.number}"

class Admin(User):
    def __init__(self, ism, familiya, passport, tyil, email, number):
        super().__init__(ism, familiya, passport, tyil, email, number)
    def ban_user(self):
        return f'User {self.ism.title()} blocked!'
admin1 = Admin('Ali','Usmonjonov','UZ000777',2009,'kamoliddinusmonjonov@gamil.com',+998772550113)
print(admin1.ban_user())