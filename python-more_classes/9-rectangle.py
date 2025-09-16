#!/usr/bin/python3
"""Defines the Rectangle class."""


class Rectangle:
    """Represents a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message when an instance of rectangle is del."""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

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

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

    Returns 0 if either width or height is 0.
    """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area."""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        rect1 = rect_1.area()
        rect2 = rect_2.area()
        if rect1 >= rect2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new instance of the class with equal width and height."""
        return cls(size, size)

    def __print_rectangle(self):
        """Build a string representation of the rectangle with '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        w = self.__width
        h = self.__height
        rect_str = ''
        for i in range(h):
            for j in range(w):
                rect_str += str(self.print_symbol)
            if i != h - 1:
                rect_str += '\n'
        return rect_str

    def __str__(self):
        """Return the string representation of the rectangle."""
        return self.__print_rectangle()

    def __repr__(self):
        """Return a representation of the rectangle."""
        w = str(eval('self.width'))
        h = str(eval('self.height'))
        return 'Rectangle(' + w + ', ' + h + ')'
