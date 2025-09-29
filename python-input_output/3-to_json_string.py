#!/usr/bin/env python3
"""
Module for converting Python objects to JSON strings.
"""

from json import dumps


def to_json_string(my_obj):
    """
    Return the JSON representation of a Python object as a string.
    """

    return dumps(my_obj)
