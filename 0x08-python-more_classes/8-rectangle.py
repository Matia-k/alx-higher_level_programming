#!/usr/bin/python3
"""Defines a class - rectangle"""


class Rectangle:
    """Defines a rectangle

    Attributes:
        number_of_instances(int): the number of instances.
        print_symbol(any): symbol to print as string.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initiates a new rectangle

        Args:
            width(int): width of the new rectangle.
            height(int): height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle.

        Args:
            value(int): value to set as width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle.

        Args:
            value(int): value to set as height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area.

        Args:
            rect_1(Rectangle): rectangle 1.
            rect_2(Rectangle):rectangle 2.

        Raises:
            TypeError: if either rect_1 or rect_2 is not a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """prints the rectangle with character stored in print_symbol"""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        for h in range(self.__height):
            for w in range(self.__width):
                print("{}".format(str(self.print_symbol)), end="")
            if h == self.__height - 1:
                break
            print()
        return ("")

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
