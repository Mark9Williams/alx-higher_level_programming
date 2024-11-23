#!/usr/bin/python3
"""Writing a string to a textfile"""


def write_file(filename="", text=""):
    """Writes a string to a file and return number of characters written"""
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
