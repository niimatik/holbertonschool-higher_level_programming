#!/usr/bin/python3
"""
Module: my_list

This module defines a custom class `Mylist` that inherits from the built-in `list` class.
It includes a method to print the list elements in sorted (ascending) order.
"""

class Mylist(list):
    """
    Mylist is a subclass of the built-in list.
    
    It provides an additional method to print the list in sorted order
    without modifying the original list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        This method does not modify the original list.
        """
        if issubclass(Mylist, list):
            print(sorted(self))
