#!/usr/bin/python3
"""
Module: is_same_class

This module provides a function to check if an object is exactly an instance
of a specified class (not a subclass).
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if `obj` is exactly an instance of `a_class`, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False