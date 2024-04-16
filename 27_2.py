class Avtosalon:
    def __init__(self,name,location,avtos,working_years):
        self.name = name
        self.location = location
        self.avtos = avtos
        self.working_years = working_years
    def get_info(self):
        return f"Name:{self.name.upper()}\nLocation:{self.location}\nCars on the sale:{self.avtos.title()}\nWorking years:{self.working_years}"
    def get_name(self):
        return self.name.upper()
    def get_location(self):
        return self.location.title()
    def get_avtos(self):
        return self.avtos
    def get_workingyears(self):
        return self.working_years
