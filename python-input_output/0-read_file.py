#!/usr/bin/python3
"""
This module provides utility functions for file operations.
The `read_file` function reads the content of a file
and prints it to the console.
It is designed to handle text files encoded in UTF-8.
"""


def read_file(filename=""):
    """
    Read a file and print its content

    Args:
        filename (str, optional): The name of the file to read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read())
