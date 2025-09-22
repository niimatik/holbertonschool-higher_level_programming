#!/usr/bin/python3
"""
Module: lookup

This module provides a utility function to retrieve the list of attributes
and methods associated with a given Python object.
"""
def lookup(obj):
    """Return the list of available attributes and methodes of an object"""
    return (dir(obj))
