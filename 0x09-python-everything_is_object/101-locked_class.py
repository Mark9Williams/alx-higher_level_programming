#!/usr/bin/python3
class LockedClass:
    """Restricts the the names of new instance attributes"""
    __slots__ = ['first_name']
