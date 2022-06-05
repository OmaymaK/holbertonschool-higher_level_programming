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
    def from_json_string(json_string):
        """ truning json to list """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON representation of dict"""
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string representation of list_objs """
        inst = []
        with open(cls.__name__ + ".json", mode='w', encoding='utf-8') as f:
            if list_objs is None:
                json.dump(inst, f)
            else:
                for i in list_objs:
                    inst.append(i.to_dictionary())
                f.write(cls.to_json_string(inst))

    @classmethod
    def create(cls, **dictionary):
        """ creating instance """
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        elif cls.__name__ == "Square":
            inst = cls(1)
        inst.update(**dictionary)
        return inst
