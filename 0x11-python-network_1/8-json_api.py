#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request."""
from sys import argv
import requests


if __name__ == '__main__':
    res = requests.post('http://0.0.0.0:5000/search_user',\
    data={'q': argv[1] if len(argv) > 1 else ""})
    try:
        r = res.json()
        if r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
