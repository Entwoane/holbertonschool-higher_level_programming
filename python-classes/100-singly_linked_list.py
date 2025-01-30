#!/usr/bin/python3
"""Module for defining and working with singly linked list"""


class Node:

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data stored in the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data attribute."""

        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.

        Raises:
            TypeError: If value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node attribute."""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.
        Raises:
            TypeError: If value is not None or a Node object.
        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""

        self.__head = None

    def __str__(self):
        """Return a string representation of the list."""

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
            value (int): The value to be inserted.
        """

        new_node = Node(value)

        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
