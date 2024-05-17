#!/usr/bin/python3
""" A class that defines a square by: (based on 5-square.py)
"""



class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square instance with a given size and position.

        Args:
            size (int, optional): The size of the square (default 0).
            position (tuple, optional): The position of the square (default (0, 0)).
        Raises:
            TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
            ValueError: If size or position is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the private instance attribute: position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the private instance attribute: position"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.size * self.size

    def my_print(self):
        """Prints the square with '#' characters"""
        if self.size == 0:
            print()
            return

        if self.position[1] > 0:
            print("\n" * self.position[1], end="")

        for _ in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
