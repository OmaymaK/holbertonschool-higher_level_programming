#!/usr/bin/python3
import json
""" Task 4 """


def from_json_string(my_str):
    """ returns an object (Python data structure)
    represented by a JSON string"""
    res = json.loads(my_str)
    res1 = json.dumps(res)
    return res1
