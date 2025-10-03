from abc import ABC, abstractmethod
import math


# Shape Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter():
        pass

# Circle extends Shape
class Circle(Shape):
    def __init__(self, raduis):
        self.raduis = raduis

    def area(self):
        print(f"Circle Area : {(math.pi * self.raduis ** 2):.2f}")
    
    def perimeter(self):
        print(f"Circle Perimeter : {(2 * math.pi * self.raduis):.2f}")

# Rectangle extends Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"Rectangle Area : {self.width * self.height}")
    
    def perimeter(self):
        print(f"Rectangle Perimeter : {(self.width + self.height) * 2}")

# Main
circle = Circle(5.0)
rectangle = Rectangle(4.0, 6.0)

circle.area()
circle.perimeter()

rectangle.area()
rectangle.perimeter()