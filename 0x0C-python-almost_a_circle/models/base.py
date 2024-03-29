#!/usr/bin/python3
""" Task 1"""
import json
from os import path
import csv


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
            return "[]"
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

    @classmethod
    def load_from_file(cls):
        """ loads a list of instances from a json file """
        inst = []
        file = cls.__name__ + ".json"
        if os.path.isfile(file):
            with open(file, 'r') as f:
                res = cls.from_json_string(f.read())
                for i in res:
                    inst.append(cls.create(**i))
        return inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        writes the CSV string representation of list_objs to a file
        """
        with open(cls.__name__ + ".csv", "w", newline='') as csvfile:
            if cls.__name__ == "Rectangle":
                fld = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fld = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(csvfile, fieldnames=fld)
            writer.writeheader()
            if list_objs is not None:
                for i in list_objs:
                    writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ load from file csv """
        if path.exists(cls.__name__ + ".csv") is False:
            return []
        with open(cls.__name__ + ".csv", "r", newline='') as csvfile:
            fli = []
            reader = csv.DictReader(csvfile)
            for i in reader:
                for key, value in i.items():
                    i[key] = int(value)
                fli.append(cls.create(**i))
        return fli
