#!/usr/bin/python3
"""defines a subclass"""
from models.base import Base


class Rectangle(Base):
    """A class that inherits from another class; Base.

    Args:
        width(int): width of the rectangle.
        height(int): height of the rectangle.
        x(int): x cordinate of the rectangl.
        y(int): y cordinate of the rectangle.
        id(int): identity of the newly instantiated rectangle.

    Raises:
        TypeError: if any of the input in not an integer.
        ValueError: if either width or height is <= 0.
        ValueError: if x or y is < 0.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the x cordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) != int:
            raise TypeError("x must be and integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the y cordinate of the rectangle."""
        return self.__y

    @width.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) != int:
            raise TypeError("y must be and integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
