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
        self.size = size

    @property
    def size(self):
        """
        Getter method for size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size

        Args:
            value (int): Size of the square

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            int: Area of the square
        """
        return self.__size ** 2
