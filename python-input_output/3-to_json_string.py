#!/usr/bin/python3
"""
Module for converting Python objects to JSON strings.
"""

from json import dump


def to_json_string(my_obj):
    """Return the JSON representation of a Python object as a string."""
    return dump(my_obj)
