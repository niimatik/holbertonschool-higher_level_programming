#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an animal.

    This class serves as a blueprint for all animal types.
    Any subclass must implement the 'sound' method.
    """


    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass

class Dog(Animal):
    """
    A concrete subclass of Animal representing a dog.
    """


    def sound(self):
        """
        Implementation of the abstract 'sound' method for Dog.
        """
        return "Bark"

class Cat(Animal):
    """
    A concrete subclass of Animal representing a cat.
    """


    def sound(self):
        """
        Implementation of the abstract 'sound' method for Cat.
        """
        return "Meow"

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(f"Dog says: {dog.sound()}")
    print(f"Cat says: {cat.sound()}")
