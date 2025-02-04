#!/usr/bin/python3
"""Module to create and work with Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initialize a square with a given size.

        Args:
            size (int): The size of the square's sides.
            Must be a positive integer.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than or equal to 0.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square, calculated as size * size.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] <width>/<height>".
        """
        return f"[Square] {self.__size}/{self.__size}"
