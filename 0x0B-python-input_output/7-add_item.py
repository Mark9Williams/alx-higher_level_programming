#!/usr/bin/python3
"""Adding all arguments to python list and saving them to a file"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_to_list():
    """adds all arguments to a Python list, and then save them to a file"""
    new_list = []
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []
    new_list += existing_data + sys.argv[1:]
    save_to_json_file(new_list, "add_item.json")


add_to_list()
