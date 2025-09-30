#!/usr/bin/python3
"""
Module defining a Student class with a method to
serialize to JSON-compatible dictionary.
"""


class Student:
    """Class representing a student with basic personal information."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the instance.

        If 'attrs' is a list of strings, only attributes with names in this
        list will be included in the returned dictionary. If 'attrs' contains
        non-stringelements or is not a list, all attributes will be returned
        instead.

        Parameters:
            attrs (list[str], optional): List of attribute names to include.
            Defaults to None.
        """
        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d

                if attr in class_d:
                    sel_d[attr] = class_d[attr]
            return sel_d
        return class_d
