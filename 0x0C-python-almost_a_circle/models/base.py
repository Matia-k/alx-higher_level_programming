#!/usr/bin/python3
"""Defines a base class"""


class Base:
    """A class that will be the “base” of all other classes in this project.

    Args:
        id(int): the id of the newly instantiated base.

    Attributes:
        __nb_objects(int): the number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
