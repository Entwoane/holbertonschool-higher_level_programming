#!/usr/bin/python3
""" Module for MyList class"""


class MyList(list):
    """
    A custom list subclass that provides additional sorting functionality.

    Public instance method:
        - print_sorted(self): Prints the list in ascending order.
    """
    def print_sorted(self):
        """
        Print the list elements in ascending order without modifying
        the original list.
        """
        print(sorted(self))
