#!/usr/bin/python3
"""Module class Student"""


class Student:
    """Class to represent student"""
    def __init__(self, first_name, last_name, age):
        """Initialize new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json"""
        return self.__dict__.copy()
