#!/usr/bin/python3
"""
Module function that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """load_from_json_file"""
    with open(file, 'r', encoding='utf8') as f:
            return json.load(f)
