from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass 
    

class Rectangle(Shape):
    def __init__(self, height, width):
        
        self.height = int(height)
        self.width = int(width)
        
    def calculate_area(self):
        return self.height * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

class Circle(Shape):
    def __init__(self, radius):
        
        self.radius = int(radius)
        
    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius
        
        
shapes = [
    Rectangle(4, 5),
    Circle(3)
]

for shape in shapes:
    print("Area:", shape.calculate_area())
    print("Perimeter:", shape.calculate_perimeter())