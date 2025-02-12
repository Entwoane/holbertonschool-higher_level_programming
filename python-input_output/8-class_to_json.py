#!/usr/bin/python3
"""
This module provides a utility function for converting a class instance
to a dictionary representation suitable for JSON serialization.

The `class_to_json` function extracts the attributes of an object and
returns them as a dictionary with simple data structures.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of the object's attributes.
    """
    return obj.__dict__
