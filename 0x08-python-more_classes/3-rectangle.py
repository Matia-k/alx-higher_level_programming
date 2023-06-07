#!/usr/bin/python3
"""Defines a class - rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initiates a new rectangle

        Args:
            width(int): width of the new rectangle.
            height(int): height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle.

        Args:
            value(int): value to set as width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle.

        Args:
            value(int): value to set as height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """prints the rectangle with character #"""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        for h in range(self.__height):
            for w in range(self.__width):
                print("#", end="")
            if h == self.__height - 1:
                break
            print()
        return ("")
