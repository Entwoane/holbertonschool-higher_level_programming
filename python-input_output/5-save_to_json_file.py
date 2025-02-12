#!/usr/bin/python3
"""
This module provides a utility function for saving
Python objects to a file in JSON format.

The `save_to_json_file` function writes a Python
object to a text file using its JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation

    Args:
        my_obj (object): The Python object to write to the file
        filename (str): The name of the file to write to
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
