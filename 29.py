class Avto:
    def __init__(self,model, colour, mode, company,price):
        self.model = model
        self.colour = colour
        self.mode = mode
        self.price = price
        self.company = company
        self.mileage = 0
        self.accidents = 0
    def get_info(self):
        return f"Company:{self.company.upper()}\nModel:{self.model.title()}\nMode:{self.mode.title()}\nColour:{self.colour.title()}\nPrice:{self.price}"
    def get_model(self):
        return f"Manufacturer company:{self.company}\nModel:{self.model}"
    def get_colour(self):
        return self.colour
    def get_price(self):
        return self.price
    def get_company(self):
        return self.company
    def set_mode(self):
        return self.mode.title()
    def get_history(self):
        return f"Milage:{self.mileage}\nAccidents:{self.accidents}"
    def update_mileage(self):
        self.mileage += 1000
def see_methods(klass):
       return [method for method in dir(klass) if method.startswith('__') is False]
avto1 = Avto('Malibu 2', 'black', 'auto','GM',27000)
avto2 = Avto('Nexia 2','blue','manual','GM',7000)
avto3 = Avto('Malibu 2','white', 'auto','GM',25000)
print(avto1.get_info())
print(avto2.get_model())
print(avto3.set_mode())
print(see_methods(Avto))