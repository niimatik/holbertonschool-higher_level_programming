#!/usr/bin/python3
"""
Module for loading a Python object from a JSON file.
"""

from json import loads


def load_from_json_file(filename):
    """Load and return a Python object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON data.

    Returns:
        object: The Python object represented by the JSON content.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
        OSError: If there is an error reading the file.
    """
    with open(filename, encoding="utf-8") as f:
        return loads(f.read())
