#!/usr/bin/python3
"""
Module rectangle
"""

from models.base import Base


class Rectangle(Base):
    """ class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initicalize rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter width"""
        return self.__width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for the y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        func to return area of rectngle
        """
        return self.__width * self.__height

    def display(self):
        """
        func to print on stdout a rectangle
        """
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """
        func to override return a  str
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        func update taht update a dict of kwargs
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        function to a dictionary represemtation
        """
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["width"] = self.width
        dict_rep["height"] = self.height
        dict_rep["x"] = self.x
        dict_rep["y"] = self.y
        return dict_rep
