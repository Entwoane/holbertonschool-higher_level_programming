#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    Enforces the implementation of `area`
    and `perimeter` methods in subclasses.
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Subclasses must override this method.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Subclasses must override this method.
        """
        pass


class Circle(Shape):
    """
    Represents a circle. Inherits from the abstract Shape class.
    """
    def __init__(self, radius):
        """
        Initializes a Circle object with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculates and returns the area of the circle.

        Formula:
            Area = π * radius^2

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius**2

    def perimeter(self):
        """
        Calculates and returns the perimeter (circumference) of the circle.

        Formula:
            Perimeter = 2 * π * radius

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle. Inherits from the abstract Shape class.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Formula:
            Area = width * height

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Formula:
            Perimeter = 2 * (width + height)

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape object.

    This function uses duck typing to call `area` and `perimeter` methods
    on any object passed to it, as long as those methods are implemented.

    Args:
        shape (Shape): An object representing a geometric shape. Must implement
                       `area` and `perimeter` methods.

    Example:
        >>> circle = Circle(radius=5)
        >>> shape_info(circle)

    Output:
       Area: <calculated area>
       Perimeter: <calculated perimeter>

       Works for any custom shapes implementing those methods!

   """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
