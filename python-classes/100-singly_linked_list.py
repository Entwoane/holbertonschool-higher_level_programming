#!/usr/bin/python3
"""
This module defines a singly linked list and its associated Node class.

The Node class represents an individual element in the linked list, while
the SinglyLinkedList class provides functionality to manage and manipulate
a sorted singly linked list.
"""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data stored in the node.
            next_node (Node): The next node in the list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data stored in the node.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Args:
            value (int): The new data value for the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list.

        Returns:
            Node: The next node in the list, or None if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The new next node for this node (or None).

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a sorted singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """
        Return a string representation of the list.

        Each node's data is printed on a new line.

        Returns:
            str: A string with each node's data on a separate line.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to be inserted into the list.

        The list remains sorted in increasing order after insertion.
        """
        new_node = Node(value)

        # Insert at the beginning if the list is empty or
        # if value is smaller than head's data
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Traverse to find the correct position for insertion
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        # Insert new_node at its correct position
        new_node.next_node = current.next_node
        current.next_node = new_node
