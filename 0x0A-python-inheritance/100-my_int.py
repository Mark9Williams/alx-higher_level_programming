#!/usr/bin/python3
"""Implementation of MyInt class"""


class MyInt(int):
    """MyInt class that inherits from int class"""

    def __eq__(self, other):
        """== inverted with !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """!= switched with =="""
        return super().__eq__(other)
