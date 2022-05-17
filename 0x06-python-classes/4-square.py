#!/usr/bin/python3
"""task4"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """inisialising"""
        self.__size = size

    def area(self):
        """getting size square"""
        return self.__size ** 2

    @property
    def size(self):
        """do size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            """return the square"""
            self.__size = value
