#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square with optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square with validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
            return None
        for i in range(1, self.area() + 1):
            print('#', end='')
            if i % self.__size == 0 and i > 0:
                print()
