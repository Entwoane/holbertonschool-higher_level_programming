#!/usr/bin/python3
"""Module for print_square method"""


def print_square(size):
    """
    Print a square of (size) length with character #

    Args:
        size (int): Size length of the square

    Returns:
        square with the character #

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float and less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for y in range(size):
        for x in range(size):
            print("#", end="")
        print()
