#!/usr/bin/python3
"""Module for defining and working with rectangle object"""


class Rectangle:
    """
    Class representing a rectangle shape
    This class allows creation and manipulation of rectangle
    objects with a specified size
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        Args:
            width (int): width of the rectangle. Defaults to 0.
            height (int): height of the rectangle. Defaults to 0.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
