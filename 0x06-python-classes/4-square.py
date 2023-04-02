#!/usr/bin/python3
"""Defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size(int): size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size of the squre.

        Args:
            value(int): value to set as size.
        """
        if type(value) != int:
            raise TypeError("Size must be an integer")
        if (value < 0):
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square"""
        return (self.__size**2)
