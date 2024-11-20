#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """Restricts the the names of new instance attributes"""
    __slots__ = ['first_name']
