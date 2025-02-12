#!/usr/bin/python3
"""
This module provides a utility function for writing text to a file.

The `write_file` function writes a string to a text file encoded in UTF-8
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns
    the number of characters written.

    Args:
        filename (str, optional): The name of the file to write to.
        If the file does not exist, it will be created.
        If it exists, its content will be overwritten.
        Defaults to "".
        text (str, optional): The string to write to the file.
        Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        write_file = file.write(text)
    return write_file
