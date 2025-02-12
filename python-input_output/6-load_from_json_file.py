#!/usr/bin/python3
"""
This module provides a utility function for loading
Python objects from a JSON file.

The `load_from_json_file` function reads a JSON file
and creates the corresponding Python object.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename (str): The name of the file to read from

    Returns:
        object: The object represented by the JSON file
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
