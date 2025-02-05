#!/usr/bin/python3
"""This module defines an abstract base class `Animal`
and its concrete subclasses `Dog` and `Cat`.

The `Animal` class serves as a blueprint for all animal types,
requiring subclasses to implement
the `sound` method. The `Dog` and `Cat` classes inherit from
`Animal` and provide specific
implementations of the `sound` method.

Classes:
    - Animal: Abstract base class for animals.
    - Dog: Concrete subclass representing a dog.
    - Cat: Concrete subclass representing a cat.

Usage Example:
    from task_00_abc import Dog, Cat

    bobby = Dog()
    garfield = Cat()

    print(bobby.sound())  # Output: Bark
    print(garfield.sound())  # Output: Meow
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    This class defines a blueprint for all animals, requiring subclasses
    to implement the `sound` method.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.

        Returns:
            str: The sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Concrete subclass of Animal representing a dog.

    Implements the `sound` method to return the sound made by a dog.
    """
    def sound(self):
        """
        Returns the sound made by a dog.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete subclass of Animal representing a cat.

    Implements the `sound` method to return the sound made by a cat.
    """

    def sound(self):
        """
        Returns the sound made by a cat.

        Returns:
            str: "Meow"
        """
        return "Meow"
