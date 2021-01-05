#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Taks: 6-square.py

This module contain a class

Class define a square with:
*private  attribute size
*istantiation with optional size: def __init__(self, size=0)
"""


class Square:
    """
    This is a class Square that defines a square

    Attributes:
        __size (int): The size of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The method __init__ for the class

        Parameters:
            size (int): size of a square.
            position (tuple): the position of square
        """
        self.size = size
        self.position = position

    def area(self):
        """
        This function calculate the area of a square

        Return:
            The area of a square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Just a property"""
        return self.__size

    @size.setter
    def size(self, value):
        """just a property setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Function that print stdout the square
        with character #
        """
        if self.__size is 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """ Just a property"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or \
           len(value) is not 2 or \
           any(map(lambda x: type(x) is not int or x < 0, value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
