#!/usr/bin/python3
""" Task 7 """


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    res = load_from_json_file(filename)
except FileNotFoundError:
    res = []

save_to_json_file(res + argv[1:], filename)
