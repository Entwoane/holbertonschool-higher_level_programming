#!/usr/bin/python3
"""Module for lookup function"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: Any Python object (e.g., module, class, instance, etc.)

    Returns:
        list: A sorted list of strings, representing the attributes and methods
              of the input object.
    """
    return dir(obj)
