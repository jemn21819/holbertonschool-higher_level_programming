#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Taks: 1-square.py

This module contain a class
that define a square with a
private  attribute size
"""


class Square:
    """
    This is a class Square that defines a square

    Attributes:
        __size (any): The size of a square
    """
    def __init__(self, size):
        """
        The method __init__ for the class

        Parameters:
            size (any): size of a square.
        """
        self.__size = size
