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
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,\
                                                         self.y, self.height)

    @property
    def size(self):
        """ size property """
        return self.width

    @size.setter
    def size(self, s):
        """ size setter """
        self.width = s
        self.height = s

    def update(self, *args, **kwargs):
        """ assigns attributes """
        attrb = ["id", "size", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, attrb[i], args[i])
        else:
            for j in kwargs:
                setattr(self, j, kwargs[j])

    def to_dictionary(self):
        """ square dict """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
