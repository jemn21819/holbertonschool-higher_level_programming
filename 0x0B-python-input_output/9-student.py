#!/usr/bin/python3
"""
Module contain class Student
"""


class Student:
    """Class for student"""
    def __init__(self, first_name, last_name, age):
        """initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json"""
        return self.__dict___.copy()
