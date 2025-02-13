#!/usr/bin/python3
"""
This module defines a CustomObject class that can be serialized
and deserialized.

The CustomObject class represents a person with attributes like name,
age, and student status.
It provides methods for displaying object information,
serialization, and deserialization.
"""


import pickle


class CustomObject:
    """
    A class representing a person with serialization capabilities.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student or not.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the CustomObject instance."""
        print(f"Name: {self.name}", )
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the CustomObject instance and save it to a file.

        Args:
            filename (str): The name of the file to save
            the serialized object to.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file.

        Args:
            filename (str): The name of the file to load the
            serialized object from.

        Returns:
            CustomObject or None: The deserialized CustomObject
            instance if successful, None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
        except pickle.UnpicklingError:
            return None
