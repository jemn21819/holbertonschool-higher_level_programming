#!/usr/bin/python3
"""Module add_atribute"""


def add_attribute(obj, attr, value):
    """add_attribute"""
    if not isinstance(attr, str) or \
       hasattr(obj, attr) or not\
       hasattr(obj, "__setattr__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
