class New_student:
    
    def __init__(self,name,fname,byear):
        self.name = name
        self.fname = fname
        self.byear = byear
        
    def get_name(self):
        return self.name
    
    def get_fname(self):
        return self.fname
    
    def get_age(self,cyear = 2024):
        return cyear-self.byear
    
    def get_all(self):
        return f"My name is {self.name} {self.fname}.I was born in {self.byear}."
    
student1 = New_student('Ali','Usmonjonov',2009)
student2 = New_student('Alisher','Olimov',2004)
student3 = New_student('Umar','Halimov',2011)
