#!/usr/bin/python3
"""
Module read a file
"""


def read_file(filename=""):
    """Func print standar output"""
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end="")
