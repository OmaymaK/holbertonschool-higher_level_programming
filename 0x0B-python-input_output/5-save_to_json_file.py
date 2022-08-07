#!/usr/bin/python3
""" Task 5 """
import json


def save_to_json_file(my_obj, filename):
    """ Writing an object to a text file using JSON """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
