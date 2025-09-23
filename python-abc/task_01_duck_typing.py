#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Requires implementation of area() and perimeter() methods.
    """


    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        Must be overridden by subclasses.
        """
        pass
    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        Must be overridden by subclasses.
        """
        pass
class Circle(Shape):
    """
    Circle shape implementing the Shape interface.
    """


    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.
        """
        self.__radius = radius
    def area(self):
        """
        Compute the area of the circle: π * r^2
        """
        return math.pi * self.__radius ** 2
    def perimeter(self):
        """
        Compute the perimeter (circumference) of the circle: 2 * π * r
        """
        return 2 * math.pi * self.__radius
    
class Rectangle(Shape):
    """
    Rectangle shape implementing the Shape interface.
    """


    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.
        """
        self.__width = width
        self.__height = height
    def area(self):
        """
        Compute the area of the rectangle: width * height
        """
        return self.__width * self.__height
    def perimeter(self):
        """
        Compute the perimeter of the rectangle: 2 * (width + height)
        """
        return 2 * (self.__width + self.__height)
def shape_info(Shape):
    """
    Print the area and perimeter of a given shape object.
    """
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
