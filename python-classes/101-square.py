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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square

        Args:
            size(int): Size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            int: Area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """
        Print a square with # character
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" "*self.position[0] + "#"*self.size)

    def __str__(self):
        """
        Define the string representation of a Square instance.

        Returns:
            str: A string representation of the square using '#' and spaces.

        Mimics my_print() behavior.
        """
        if self.__size == 0:
            return ""

        result = []
        result.extend([""]*self.__position[1])
        for _ in range(self.__size):
            result.append(" "*self.__position[0] + "#"*self.__size)
        return "\n".join(result)
