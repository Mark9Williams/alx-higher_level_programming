#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """Inherits all the methods and attributes of the list class"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
