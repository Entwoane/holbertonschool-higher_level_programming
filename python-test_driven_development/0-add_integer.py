#!/usr/bin/python3
"""Module for add integer method"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: first number
        b=98: second number. Default to 98.

    Returns:
        int: sum of a and b

    Raises:
        TypeError: If a or b is not an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
