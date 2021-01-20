#!/usr/bin/python3
"""
Module function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """ return numbers of chara writtrn"""
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
