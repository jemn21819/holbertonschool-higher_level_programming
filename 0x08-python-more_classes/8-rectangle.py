#!/usr/bin/python3
"""
Module of empty class rectangle
"""


class Rectangle:
    """ Empty Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            rec += str(self.print_symbol) * self.__width + '\n'
        return rec[:-1]

    def __repr__(self):
        """ return representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return biggest rect area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
