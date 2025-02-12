#!/usr/bin/python3
"""
This module defines a `Student` class with attributes
for first name, last name, and age.

The `Student` class includes a method to retrieve a
dictionary representation of its attributes, making it suitable for
JSON serialization or other uses.
"""


class Student:
    """
    A class that defines a student with first name, last name, and age.
    Provides a method to retrieve a dictionary representation of the instance.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing all attributes of the instance.
        """
        return self.__dict__
