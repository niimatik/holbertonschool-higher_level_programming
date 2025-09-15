#!/usr/bin/python3
"""Defines the Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not self.__check_int(value):
            raise TypeError("width must be an integer")
        if not self.__check_positive(value):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not self.__check_int(value):
            raise TypeError("height must be an integer")
        if not self.__check_positive(value):
            raise ValueError("height must be >= 0")
        self.__height = value

    def __check_int(self, value):
        """Check if value is an integer."""
        return isinstance(value, int)

    def __check_positive(self, value):
        """Check if value is non-negative."""
        return value >= 0
