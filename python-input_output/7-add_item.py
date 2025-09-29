#!/usr/bin/python3
"""
Script that adds command-line arguments to a JSON list stored in a file.

- Loads the list from 'add_item.json' if it exists.
- Appends all arguments passed to the script.
- Saves the updated list back to 'add_item.json'.
"""

from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists('add_item.json'):
    obj = load_from_json_file('add_item.json')
else:
    obj = []

for i in range(1, len(argv)):
    obj.append(argv[i])

save_to_json_file(obj, 'add_item.json')
