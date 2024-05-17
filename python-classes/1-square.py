#!/usr/bin/python3
"""
Square with size
A class Square that defines a square
"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size: int):
        """Initialize the Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
