from abc import ABC, abstractmethod

from math import pi

class Shape(ABC):
        
    pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius 
    
    def calculate_perimeter(self):
        return 2 * pi * self.radius

    def calculate_area(self):
        return pi * self.radius **2

class Square(Shape):

    def __init__(self, side):
        self.side= side
    
    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side **2

class Rectangle(Shape):

    def __init__(self, width, heigth):
        self.width= width
        self.heigth= heigth

    
    def calculate_perimeter(self):
        return 2 * (self.width + self.heigth)

    def calculate_area(self):
        return self.width * self.heigth
    


circle = Circle(15)
print(f"The Circle´s area is: {circle.calculate_area()}")
print(f"The Circle´s perimeter is: {circle.calculate_perimeter()}")

square= Square(8)
print(f"The Square´s area is: {square.calculate_area()}")
print(f"The Square´s perimeter is: {square.calculate_perimeter()}")

rectangle= Rectangle(45,30)
print(f"The Rectangle´s area is: {rectangle.calculate_perimeter()}")
print(f"The Rectangle´s perimeter is: {rectangle.calculate_area()}")



    

