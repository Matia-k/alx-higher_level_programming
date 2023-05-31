#!/usr/bin/python3
"""Defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.

        Args:
            size(int): size of the new square.
            position(tuple): position of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size of the square.

        Args:
            value(int): value to set as size.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the position of the square.

        Args:
            value(tuple): cordinates to set position at.
        """
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of \
                    2 positive integers")
        for n in value:
            if not isinstance(n, int):
                raise TypeError("position must be a tuple of \
                        2 positive integers")
            if n < 0:
                raise TypeError("position must be a tuple of \
                        2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        i = 0
        if (self.__size == 0):
            print()
        else:
            for h in range(self.__position[1]):
                print()
            while (i < self.__size):
                for k in range(self.__position[0]):
                    print(f" ", end="")
                for j in range(self.__size):
                    print(f"#", end="")
                print()
                i = i + 1

    def area(self):
        """Returns the current area of the square"""
        return (self.__size**2)
