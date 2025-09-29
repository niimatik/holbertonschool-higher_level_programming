#!/usr/bin/python3
"""
Module for reading and printing the contents of a text file.

This module defines a function `read_file` that reads a UTF-8 encoded text file
and prints its contents to standard output.

Functions:
    read_file(filename=""): Opens a file and prints its content to stdout.
"""


def read_file(filename=""):
    """Read a file and print its output."""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
