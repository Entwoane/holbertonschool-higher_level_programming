#!/usr/bin/python3


class CountedIterator:
    """
    A class that wraps an iterator and counts the number
    of items iterated over.
    """
    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.

        Args:
            iterable: Any iterable object (e.g., list, tuple, set).
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the current count of items iterated.

        Returns:
            int: The number of items iterated so far.
        """
        return self.counter

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.

        Returns:
            The next item from the wrapped iterator.

        Raises:
            StopIteration: When there are no more items in the iterator.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns itself as an iterator.

        Returns:
            CountedIterator: The instance itself.
        """
        return self
