#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Taks: 4-square.py

This module contain a class

Class define a square with:
*private  attribute size
*nstantiation with optional size: def __init__(self, size=0)
"""


class Square:
    """
    This is a class Square that defines a square

    Attributes:
        __size (int): The size of a square
    """
    def __init__(self, size=0):
        """
        The method __init__ for the class

        Parameters:
            size (int): size of a square.
        """
        self.__size = size

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
