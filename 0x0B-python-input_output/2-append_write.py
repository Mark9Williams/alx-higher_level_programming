#!/usr/bin/python3
"""Appending a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file"""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
