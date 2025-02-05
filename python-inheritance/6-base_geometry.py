#!/usr/bin/python3
"""Module to create ans work with BaseGeometry"""


class BaseGeometry:
    """A base class for geometry-related operations.
    """
    def area(self):
        """
        Raise an exception indicating that the area method is not implemented.

        Raises:
            Exception: Always raises an exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")
