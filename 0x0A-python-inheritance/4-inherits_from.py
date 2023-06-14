#!/usr/bin/python3
"""Defines a function that checks for an inherited class"""


def inherits_from(obj, a_class):
    """checks if an object inherited from a subclass of a given class

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
