#!/usr/bin/python3
"""task3"""


class Square:
    """class square that defines a square"""

    def __init__(self, size=0):
        """inisialisation"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """returning square"""
            return self.__size ** 2