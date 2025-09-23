#!/usr/bin/python3
class SwimMixin:
    """
    Mixin class that provides swimming capability.
    """

    def swim(self):
        """
        Print a message indicating that the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capability.
    """

    def fly(self):
        """
        Print a message indicating that the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that can both swim and fly,
    by inheriting from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Print a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")
