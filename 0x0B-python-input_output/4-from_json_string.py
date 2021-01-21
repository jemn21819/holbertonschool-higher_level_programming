#!/usr/bin/python3
"""
module  function that returns an object
"""
import json


def from_json_string(my_str):
    """from_json_string"""
    return json.loads(my_str)
