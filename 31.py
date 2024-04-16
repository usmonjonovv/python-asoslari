from uuid import uuid4
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
    
class User(Shaxs):
    __foydalanuvchi_soni = 0
    def __init__(self, ism, familiya, passport, tyil,email,number):
        super().__init__(ism, familiya, passport, tyil)
        self.email = email
        self.number = number
        self.__id = uuid4()
        User.__foydalanuvchi_soni += 1

    def get_id(self):
        return self.__id

    def get_email(self):
        return self.email
    
    def get_number(self):
        return self.number
    
    def get_all(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Foydalanuvchi elektron pochtasi: {self.email}"
        info += f"Foydalanuvchi raqami: {self.number}"

    @classmethod
    def get_foydalanuvchi_soni(cls):
        return cls.__foydalanuvchi_soni