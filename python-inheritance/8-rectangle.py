#!/usr/bin/python
"""Module to create and work with BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            Must be a positive integer.
            height (int): The height of the rectangle.
            Must be a positive integer.

        Raises:
            TypeError: If `width` or `height` is not an integer.
            ValueError: If `width` or `height` is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
