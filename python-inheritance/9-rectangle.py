#!/usr/bin/python3
"""
Module: rectangle

This module defines a Rectangle class that inherits from BaseGeometry.
It validates width and height using BaseGeometry's integer_validator method.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height
    
    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return '[rectangle]' + str(self.__width) + '/' + str(self.__height)
