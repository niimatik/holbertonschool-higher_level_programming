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

    def to_json(self):
        """Return a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary of the instance attributes.
        """
        return self.__dict__
