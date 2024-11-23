#!/usr/bin/python3
"""Reading text file and printing it to standard output"""


def read_file(file_name="", encoding="utf-8"):
    """reads a text file and prints it to stdout"""
    with open(file_name) as f:
        print(f.read(), end="")
