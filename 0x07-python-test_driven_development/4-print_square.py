#!/usr/bin/python3
"""
task: 4-print_square.py
This module print a square with #
"""


def print_square(size):
    """ print_square

    Args:
    size(any): size of a square

    Raise:
    TypeError: type error
    ValueError: Value Error
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
