#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'r+', encoding="utf-8") as f:
        return len(f.write(text))
