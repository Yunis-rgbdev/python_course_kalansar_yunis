class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def display_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"
    
class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors
        
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Number of Doors: {self.num_doors}"
    
class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
    
    def display_info(self):
        base_info = super().display_info()
        sidecar_info = "Yes" if self.has_sidecar else "No"
        return f"{ base_info }, Has sidecar: { sidecar_info}"
    
    
# Example usage:

vehicle = Vehicle("Generic", 2000)
car = Car("Toyota", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", 2019, False)

print(vehicle.display_info())
print(car.display_info())
print(motorcycle.display_info())