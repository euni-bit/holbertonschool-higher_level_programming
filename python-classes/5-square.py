#!/usr/bin/python3
""" A class that defines a square by: (based on 4-square.py)
"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0):
        """Define Private instance attribute: size"""
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

    def my_print(self):
        """Prints a square using '#' characters"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
