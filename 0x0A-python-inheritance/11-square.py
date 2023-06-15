#!/usr/bin/python3
"""Defines a class square that inherits from a rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square.

    Args:
        size(int): the size of the square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
