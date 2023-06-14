#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """A class representing BaseGeometry"""

    def area(self):
        """raises a given exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Ags:
            name(str): name of the parameter.
            value(int): value stored by name.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
