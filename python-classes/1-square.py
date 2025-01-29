#!/usr/bin/python3
"""Module for defining and working with square object"""


class Square:
    """
    Class representing a square shape
    This class allows creation and manipulation of square
    objects with a specified size

    Attributes:
        __size: size of the square (private)

    """
    def __init__(self, size):
        """
        Initialize a new square

        Args:
            size: Size of the square
        """
        self.__size = size
