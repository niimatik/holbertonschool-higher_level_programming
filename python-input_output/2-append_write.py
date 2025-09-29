#!/usr/bin/python3
"""
Module for appending text to a file.
Provides a function `append_write` that adds content to the end of a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """
    Append text to the end of a file and return the number
    of characters written.
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
