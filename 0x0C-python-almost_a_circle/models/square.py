#!/usr/bin/python3
""" Task 10 """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialsation for the square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str method """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.height)
