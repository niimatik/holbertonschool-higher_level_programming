#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if self.__check_tuple(position) is False \
            or self.__check_indexes(position) is False \
            or self.__check_integers(position) is False \
            or self.__check_value(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        
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
        """get the position of the square"""
        return self.__position
    
    @position.setter
    def position(self, position):
        """Set the position of the square with validation."""
        if self.__check_tuple(position) is False \
            or self.__check_indexes(position) is False \
            or self.__check_integers(position) is False \
            or self.__check_value(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def __check_tuple(position):
        if position is tuple:
            return True
        return False

    def __check_indexes(position):
        if len(position) == 2:
            return True
        return False

    def __check_integers(position):
        if type(position[0]) is int and type(position[1]) is int:
            return True
        return False
    
    def __check_value(position):
        if position[0] >= 0 and position[1] >= 0:
            return True
        return False

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
