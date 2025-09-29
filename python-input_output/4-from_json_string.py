#!/usr/bin/python3
"""
Module for return Python objects represented by JSON string.
"""
from json import loads


def from_json_string(my_str):
    """Return an object represented by a json string"""
    return loads(my_str)
