#!/usr/bin/python3
"""Module to create ans work with BaseGeometry"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class serves as a blueprint for creating geometry-related classes. It includes:
    - An `area` method that is intended to be overridden by subclasses.
    - An `integer_validator` method to validate positive integer values.

    Methods:
        - area(self): Raises an exception indicating that the method is not implemented.
        - integer_validator(self, name, value): Validates that the given value is a positive integer.
    """
    def area(self):
        """
        Raise an exception indicating that the area method is not implemented.

        Raises:
            Exception: Always raises an exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the parameter (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
