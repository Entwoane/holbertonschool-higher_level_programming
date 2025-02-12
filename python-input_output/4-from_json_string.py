#!/usr/bin/python3
"""
This module provides a utility function for converting
JSON strings to Python objects.

The `from_json_string` function takes a JSON string and
returns the corresponding Python object.
"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: A Python object represented by the JSON string.
    """
    return json.loads(my_str)
