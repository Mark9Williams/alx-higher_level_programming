#!/usr/bin/python3
"""Implementation of Class student"""


class Student:
    """class that defines student"""
    def __init__(self, first_name, last_name, age):
        """instantiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a student"""
        return self.__dict__
