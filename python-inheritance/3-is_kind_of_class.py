#!/usr/bin/python3
"""
Module: is_kind_of_class

This module provides a function that checks if an object is an instance
of a class or of a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or its subclasses.
    """
    return isinstance(obj, a_class)
