#!/usr/bin/python3
"""
Module contain class Mylist
"""


class MyList(list):
    """MyList class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """ function print sorted list"""
        print(sorted(self))
