#!/usr/bin/python3
"""inserting a line of text to a file, after each line"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
