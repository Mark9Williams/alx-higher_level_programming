#!/usr/bin/python3
"""Writing an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
