#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Taks: 2-square.py

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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
