#!/usr/bin/python3
"""A Python script that takes in a URL."""


from urllib import request, error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as url:
            print(url.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
