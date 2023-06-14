#!/usr/bin/python3
"""Defines a class that inherits from another class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle and inherits from BaseGeometry.

    Args:
        width(int): width of the rectangle.
        height(int): height of the rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
