#!/usr/bin/python3
"""
Module: square

This module defines a Square class that inherits from Rectangle.
It ensures the size is validated and passed as both width and height
to the parent Rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    def __init__(self, size):
        """Initializes a Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
