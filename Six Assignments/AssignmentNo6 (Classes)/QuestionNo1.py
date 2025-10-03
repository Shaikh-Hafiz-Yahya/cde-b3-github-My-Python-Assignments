# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
        
obj:Circle = Circle(3)        
print(obj.area())
print(obj.perimeter())
print(obj.radius)


