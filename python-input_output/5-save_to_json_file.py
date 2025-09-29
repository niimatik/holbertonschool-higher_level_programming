#!/usr/bin/python3
"""
Module for saving Python objects to a file in JSON format.
"""

from json import dumps


def save_to_json_file(my_obj, filename):
    """Serialize a Python object to a JSON file using UTF-8 encoding.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file to write the JSON data to.

    Raises:
        TypeError: If the object is not JSON serializable.
        OSError: If the file cannot be created or written to.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(dumps(my_obj))
