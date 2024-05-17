#!/usr/bin/python3
"""
Access and update private attribute
Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0):
        """Initialize a square instance with a given size.

        Args:
            size (int): The size of the square (default 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    def area(self):
        """Returns the current square area"""
        return self.size * self.size

    @property
    def size(self):
        """Retrieve the private instance attribute: size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private instance attribute: size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
