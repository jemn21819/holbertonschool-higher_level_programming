#!/usr/bin/python3
"""Define a class MagicClass"""
import math


class MagicClass:
    """class that represents a cirlce"""
    def __init__(self, radius=0):
        """Initialize with default radius=0

        __init__ method initializes radius and test if numeric"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate area based on radius"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate circumference with given radius"""
        return 2 * math.pi * self.__radius
