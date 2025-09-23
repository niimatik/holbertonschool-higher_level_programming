#!/usr/bin/python3

class VerboseList(list):
    """
    A subclass of Python's built-in list that prints messages
    whenever items are added or removed.
    """

    def append(self, item):
        """
        Add a single item to the list and print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from another iterable and print a message.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of item and print a message.
        If item is not found, ValueError will be raised (default behavior).
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at index (default last).
        Print the item being popped.
        """
        item = self[index]  # Get item before removal
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
