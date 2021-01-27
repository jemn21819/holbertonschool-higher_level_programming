#!/usr/bin/python3

"""
Module with calss Base
"""

import json
import csv


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization of the class Base
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        f_name = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(f_name, 'w') as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load from a file json
        """
        f_name = cls.__name__ + ".json"
        list_inst = []
        try:
            with open(f_name, 'r') as f:
                list_inst = cls.from_json_string(f.read())
            for i, j in enumerate(list_inst):
                list_inst[i] = cls.create(**list_inst[i])
        except:
            pass
        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes a list of Rectangles/Squares in csv
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes a list of Rectangles/Squares in csv
        """
        filename = cls.__name__ + ".csv"
        l = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    l.append(obj)
        except:
            pass
        return l
