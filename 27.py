class Users:
    def __init__(self,name,fname,username,age,email):
        self.name = name
        self.fname = fname
        self.username = username
        self.age = age
        self.email = email
    def get_info(self):
        return f"User:{self.username}\nFullname:{self.name.title()} {self.fname.title()}\nAge:{self.age}\nEmail:{self.email}"
    def get_fullname(self):
        return f"{self.name.title()} {self.fname.title()}" 
    def get_username(self):
        return self.username
    def get_email(self):
        return self.email
user1 = Users("olim","olimov",'olimolimov1995',19,'olimolimov1995@rumail.com')
user2 = Users("husan","akbarov",'husanakbarov2004',20,'husanakbarov2004@hotmail.com')
user3 = Users("hasan","akbarov",'hasanakbarov2022',20,'hasanakbarov2022@gmail.com')
print(user2.get_info())