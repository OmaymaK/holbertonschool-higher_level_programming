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
