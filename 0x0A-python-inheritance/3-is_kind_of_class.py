#!/usr/bin/python3
"""Defineds an inherited class"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of a_class or of parent of a_class.

    Args:
        obj: the object to check.
        a_class: class to compare type of obj to.

    Returns:
        bool: True if the object is an instance of, False otherwise.
    """
    return isinstance(obj, a_class)
