#!/usr/bin/python3
"""
This module provides a utility function for appending text to a file.

The `append_write` function appends a string to
the end of a text file encoded in UTF-8 and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8) and returns the
    number of characters added.

    Args:
        filename (str, optional): The name of the file to append to.
        If the file does not exist, it will be created.
        Defaults to "".
        text (str, optional): The string to append to the file.
        Defaults to "".

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        append_file = file.write(text)
    return append_file
