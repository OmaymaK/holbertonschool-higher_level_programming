#!/usr/bin/python3
""" Task 1"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON representation """
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)
