#!/usr/bin/python3
class Fish:
    """
    Represents a basic fish.

    Provides methods for fish-like behaviors such as swimming and indicating habitat.
    """

    def swim(self):
        """
        Print a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message indicating the habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a basic bird.

    Provides methods for bird-like behaviors such as flying and indicating habitat.
    """

    def fly(self):
        """
        Print a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message indicating the habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish, which can both swim like a fish and fly like a bird.

    Inherits from both Fish and Bird classes, overriding methods to reflect its unique capabilities.
    """

    def fly(self):
        """
        Print a custom message indicating that the flying fish is soaring through the air.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Print a custom message indicating that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Print a message indicating that the flying fish lives in both water and sky environments.
        """
        print("The flying fish lives both in water and the sky!")
