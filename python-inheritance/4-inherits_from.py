#!/usr/bin/python3
"""
Module: inherits_from

This module provides a function that checks if an object is an instance of
a subclass of a given class (but not an instance of the class itself).
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a subclass of the specified class.
    """
    if isinstance(obj, a_class) and \
        issubclass(a_class, obj.__class__) is False:
        return True
    return False
