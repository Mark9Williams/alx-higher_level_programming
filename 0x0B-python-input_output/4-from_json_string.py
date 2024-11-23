#!/usr/bin/python3
"""Converting from a JSON string to a python data structure"""
import json


def from_json_string(my_str):
    """returns an object represented as a JSON string"""
    return json.loads(my_str)
