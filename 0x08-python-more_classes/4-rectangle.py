#!/usr/bin/python3
"""
Module of empty class rectangle
"""


class Rectangle:
    """ Empty Rectangle"""
    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """some property"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """some property"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Method for calculate area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ calculate perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """print the rectangle with the character #"""
        rec = ""
        if not (self.__width and self.__height):
            return rec
        for i in range(self.__height):
            rec += '#' * self.__width + '\n'
        return rec[:-1]

    def __repr__(self):
        """ return representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
