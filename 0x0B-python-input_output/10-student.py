#!/usr/bin/python3
"""Module class Student"""


class Student:
    """Class to represent student"""
    def __init__(self, first_name, last_name, age):
        """Initialize new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json"""
        if type(attrs) is list:
            new_dict = {}
            for i in attrs:
                if type(i) is str and i in self.__dict_.keys():
                    new_dict[i] = self.__dict__.get(i)
            return new_dict
        else:
            return self.__dict__
