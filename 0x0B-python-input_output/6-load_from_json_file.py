#!/usr/bin/python3
import json
""" Task 6 """


def load_from_json_file(filename):
    with open(filename, mode="r") as f:
        res = json.load(f)
        return res
