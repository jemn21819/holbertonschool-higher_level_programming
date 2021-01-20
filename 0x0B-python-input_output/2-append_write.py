#!/usr/bin/python3
"""
Module function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Return number of chars appended to file"""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
