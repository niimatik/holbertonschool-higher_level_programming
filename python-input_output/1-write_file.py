#!/usr/bin/python3
def write_file(filename="", text=""):
    """Return the number of char print in the file."""
    with open(filename, 'r+', encoding="utf-8") as f:
        return len(f.write(text))
