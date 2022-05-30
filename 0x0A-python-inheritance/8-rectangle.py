#!/usr/bin/python3
"""Task 7"""


class BaseGeometry():
    """class"""

    def area(self):
        """area implementation"""

        raise Exception("area() is not implemented")
   
    def integer_validator(self, name, value):
        """checking if value is int and positive"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialsation"""
        self.integer_validator("width", width) 
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
