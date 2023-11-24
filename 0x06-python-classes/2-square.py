#!/usr/bin/python3
"""Module with a Square class"""


class Square:
    """
    A representation of a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        """Validates the size attribute."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
