#!/usr/bin/python3
""" Module for print_sorted function"""


class MyList(list):
    """
    A custom list subclass that provides additional sorting functionality.

    Args:
        list (int): list of integers
    """
    def print_sorted(self):
        """
        Print the list elements in ascending order without modifying
        the original list.
        """
        print(sorted(self))
