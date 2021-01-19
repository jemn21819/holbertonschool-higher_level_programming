#!/usr/bin/python3
"""
Module contain class Mylist
"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """ function print sorted list"""
        print(sorted(self))
