#!/usr/bin/python3
class CountedIterator:
    """
    An iterator wrapper that counts how many items have been iterated.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.
        """
        item = next(self.iterator)  # Raises StopIteration if no more items
        self.count += 1
        return item

    def __iter__(self):
        """
        Return the iterator itself.
        """
        return self

    def get_count(self):
        """
        Return the number of items that have been iterated over so far.
        """
        return self.count
