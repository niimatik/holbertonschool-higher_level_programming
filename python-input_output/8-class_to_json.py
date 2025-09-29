#!/usr/bin/python3
"""
Module for converting a class instance to a dictionary.
Useful for JSON serialization of objects.
"""


def class_to_json(obj):
    """Return the dictionary description of a simple data structure.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object (its __dict__).
    """
    return obj.__dict__
