#!/usr/bin/python3
"""Defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size(int): size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square"""
        return (self.__size**2)
