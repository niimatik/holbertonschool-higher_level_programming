#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def read_file(filename=""):
    """Read a file and print its output."""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
