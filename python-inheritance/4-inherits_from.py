#!/usr/bin/python3
"""Module for inherit from function"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a
        subclass of the specified class
        (but not an instance of the class itself); otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
