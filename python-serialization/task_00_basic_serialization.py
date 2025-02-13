#!/usr/bin/python3
"""
This module provides functions for serializing
and deserializing data to and from JSON files.

It contains two main functions:
- serialize_and_save_to_file: Serializes data to JSON and saves it to a file.
- load_and_deserialize: Loads and deserializes JSON data from a file.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data to JSON and save it to a file.

    Args:
        data: The data to be serialized (must be JSON-serializable).
        filename (str): The name of the file to save the data to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file.

    Args:
        filename (str): The name of the file to load data from.

    Returns:
        The deserialized data from the file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
