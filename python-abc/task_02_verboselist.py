#!/usr/bin/python3


class VerboseList(list):
    """
    A custom list class that extends Python's built-in list.
    This class prints notifications whenever items are added or removed
    using the append, extend, remove, or pop methods.
    """
    def append(self, item):
        """
        Overrides append to notify when an item is added.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """
        Overrides extend to notify when multiple items are added.
        """
        super().extend(x)
        print(f"Extended the list with [{len(x)}] items.")

    def remove(self, item):
        """
        Overrides remove to notify when an item is removed.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        Overrides pop to notify when an item is removed by index.

        Args:
            index (int): The index of the item to remove (default: last item).

        Returns:
            The popped item.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
