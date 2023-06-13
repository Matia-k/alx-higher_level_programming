#!/usr/bin/python3
"""Defines a function that checks for class of object."""


def is_same_class(obj, a_class):
    """checks if an obj is exactly an instance of a specified class.


    Args:
        obj (any): the object to check.
        a_class (type): the class to compare against.

    Returns:
        True if obj is exactly an instance of a_class.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
