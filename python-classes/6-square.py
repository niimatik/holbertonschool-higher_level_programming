#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with optional size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (not self.__check_tuple(value) or
                not self.__check_length(value) or
                not self.__check_integers(value) or
                not self.__check_non_negative(value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __check_tuple(self, value):
        """Check if value is a tuple."""
        return isinstance(value, tuple)

    def __check_length(self, value):
        """Check if tuple has exactly two elements."""
        return len(value) == 2

    def __check_integers(self, value):
        """Check if both elements are integers."""
        return all(isinstance(i, int) for i in value)

    def __check_non_negative(self, value):
        """Check if both elements are non-negative."""
        return all(i >= 0 for i in value)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters and position offset."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
