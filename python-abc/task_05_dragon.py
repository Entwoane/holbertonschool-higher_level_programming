#!/usr/bin/python3


class SwimMixin:
    """
    A mixin class that provides swimming behavior to
    any class that inherits from it.
    """

    def swim(self):
        """
        Prints a message indicating that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying behavior to
    any class that inherits from it.
    """
    def fly(self):
        """
        Prints a message indicating that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Represents a dragon, a mythical creature that can both swim and fly.

    This class inherits swimming behavior from SwimMixin
    and flying behavior from FlyMixin.
    Additionally, it defines a unique behavior for roaring.
    """
    def roar(self):
        """
        Prints a message indicating that the dragon roars.
        """
        print("The dragon roars!")
