#!/usr/bin/python3
"""
This module provides a utility function for
converting Python objects to JSON strings.

The `to_json_string` function takes a Python object
and returns its JSON representation as a string.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj (object): The Python object to convert into a JSON

    Returns:
        str: The JSON representation of the object as a string
    """
    return json.dumps(my_obj)
