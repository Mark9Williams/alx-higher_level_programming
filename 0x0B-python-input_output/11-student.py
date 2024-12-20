#!/usr/bin/python3
"""Implementation of Class student"""


class Student:
    """class that defines student"""

    def __init__(self, first_name, last_name, age):
        """instantiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student"""
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
