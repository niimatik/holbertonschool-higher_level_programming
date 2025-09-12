#!/usr/bin/python3
"""
This module defines a function `add_integer` that adds two integers or floats.

If either argument is a float, it will be converted to an integer by truncation (i.e., without rounding).
If the inputs are not integers or floats, a TypeError is raised.
"""
def add_integer(a, b=98):
    """
    Adds two numbers after validating and converting them to integers.

    Parameters:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b, both converted to integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b

def convert_to_int(num):
    """
    Converts a float to an integer by truncation. 
    If the input is already an integer, it is returned unchanged.

    Parameters:
        num (int or float): The number to convert.

    Returns:
        int: The integer value of num.
    """
    if type(num) is float:
        num = int(num)
    return (num)
