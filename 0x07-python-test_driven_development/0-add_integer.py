#!/usr/bin/python3
"""
This module contain a fucntion
thats adds 2 integers.
args a and b integers to add
"""


def add_integer(a, b=98):
    """add_integer
    returns: integer of resutl
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
