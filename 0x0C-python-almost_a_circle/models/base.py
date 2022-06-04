#!/usr/bin/python3
""" Task 1"""


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialsation """
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
