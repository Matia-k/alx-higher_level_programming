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

    def update(self, *args, **kwargs):
        """updates the attributes of the square.

        Args:
            *args(tuple): a tuple of arguments to assign as attributes.
            **kwargs(dict): key-value pairs of the new attributes.
        """
        if len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif (not args) or len(args) == 0 and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
