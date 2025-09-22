#!/usr/bin/python3
"""
Module: is_same_class

This module provides a function to check if an object is exactly an instance
of a specified class (not a subclass).
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.
    """
    return type(obj) == a_class