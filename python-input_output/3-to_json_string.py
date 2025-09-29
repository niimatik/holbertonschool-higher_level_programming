#!/usr/bin/env python
"""
Module for converting Python objects to JSON strings.
"""
from json import dumps


def to_json_string(my_obj):
    """Return the JSON representation of a Python object as a string.
    Args:
        my_obj: The Python object to convert.
    Returns:
        str: The JSON string representation of the object.
    """
    return dumps(my_obj)
