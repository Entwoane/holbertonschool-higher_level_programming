#!/usr/bin/python3
"""
This module defines a `Student` class with attributes
for first name, last name, and age.

The `Student` class includes methods to retrieve a
dictionary representation of its attributes, with an option
to filter specific attributes.
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

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing all attributes of the instance.
            If attrs is None or not a list of strings,
            all attributes are returned.
        """
        if (isinstance(attrs, list) and all(isinstance(item, str)
                                            for item in attrs)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        else:
            return self.__dict__
