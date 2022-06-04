#!/usr/bin/python3
""" Task 2 """
from models.base import Base


class Rectangle(Base):
    """ class rectangle that inherits from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialsation """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, w):
        """ width setter """
        if type(w) is not int:
            raise TypeError("width must be an integer")
        elif w <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = w

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, h):
        """ height setter """
        if type(h) is not int:
            raise TypeError("height must be an integer")
        elif h <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = h

    @property
    def x(self):
        """ x property """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """ y property """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ rectangle's area calculation """
        return self.__width * self.__height

    def display(self):
        """ rectangle representation using # character """
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
