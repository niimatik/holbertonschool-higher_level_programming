#!/usr/bin/python3
"""
Module for writing text to a file.

This module provides a function `write_file` that writes a string to a file,
creating or overwriting the file if it exists.
"""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written."""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
