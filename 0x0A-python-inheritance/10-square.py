#!/usr/bin/python3
"""Defines a square class that inherits from a rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class square that inherits from a Rectangle

    Args:
        size(int): size of the square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
