class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def displayInfo(self):
        print(f" {self.brand}, {self.model}, {self.year}")

car1 = Car("BMW", "M5", 2022)
car1.displayInfo()