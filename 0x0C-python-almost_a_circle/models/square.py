#!/usr/bin/python3
"""defines a class that inherits from another"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square.

    Args:
        size(int): the size of the square.
        x(int): the x cordinate of the square.
        y(int): the y cordinate of the square.
        id(int): the identity of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the str representation of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
