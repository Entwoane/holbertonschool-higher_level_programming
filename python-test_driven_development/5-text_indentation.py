#!/usr/bin/python3
"""Module for text_indentation method"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each ".", "?" and ":"

    Args:
        text (string): Text to indent

    Returns:
        text with correct indentation

    Raise:
        TypeError: if (text) is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    print(text.replace(". ", ".\n\n").replace
          ("? ", "?\n\n").replace(": ", ":\n\n"))
