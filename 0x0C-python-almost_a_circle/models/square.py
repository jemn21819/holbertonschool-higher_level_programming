#!/usr/bin/python3
"""
Module of a class square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization of square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        informal string of square representation
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """
        func to update assing attributes
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Func to Dictionary representation
        """
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["size"] = self.size
        dict_rep["x"] = self.x
        dict_rep["y"] = self.y
        return dict_rep
