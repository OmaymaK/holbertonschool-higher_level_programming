#!/usr/bin/python3
import json
""" Task 5 """


def save_to_json_file(my_obj, filename):
    """ Writing an object to a text file using JSON """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
