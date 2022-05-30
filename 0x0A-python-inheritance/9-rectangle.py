#!/usr/bin/python3
"""A Geometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialsation"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area calcul"""
        return (self.__height * self.__width)

    def __str__(self):
        """implementing str"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
