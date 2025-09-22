#!/usr/bin/python3
"""
Module: base_geometry

This module defines a class `BaseGeometry`.
It is intended to be used as a base class for geometric shapes.
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.

    This class should be subclassed, and the `area` method
    should be implemented by the subclasses.
    """

    def area(self):
        """
        Raises an Exception to indicate that the method is not implemented.

        This method is meant to be overridden by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a parameter is a positive integer.
        """
        if isinstance(value, int) is False:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
