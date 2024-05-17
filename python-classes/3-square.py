#!/usr/bin/python3
"""
3. Area of a square
Write a class Square that defines a square by: (based on 2-square.py)
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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size