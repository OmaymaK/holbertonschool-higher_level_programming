#!/usr/bin/python3
"""task 5"""


class Square:
    """class that defines a square"""

    def __init__(self, size=0):
        """inisialising"""
        self.__size = size

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

    def area(self):
        """getting size square"""
        return self.__size ** 2

    def my_print(self):
        """printing a square"""
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print('')
