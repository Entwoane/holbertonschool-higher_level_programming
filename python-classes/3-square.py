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
    def __init__(self, size=0):
        """
        Initialize a new square

        Args:
            size(int): Size of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            int: Area of the square
        """
        return self.__size ** 2
