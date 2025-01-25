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

    special_chars = ['.', '?', ':']
    result = []
    currentline = ""

    for char in text:
        currentline += char
        if char in special_chars:
            result.append(currentline.strip())
            result.append("")
            currentline = ""

    if currentline:
        result.append(currentline.strip())

    print('\n'.join(result))
