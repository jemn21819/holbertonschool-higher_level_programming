#!/usr/bin/python3
"""
Module  function that writes an Object to a text file, using a JSON
"""

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(my_obj)
