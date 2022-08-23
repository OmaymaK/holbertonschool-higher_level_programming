#!/usr/bin/python3
"""Sends a POST request to the passed URL."""


import requests
import sys


if __name__ == '__main__':
    requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print("Your email is: {}".format(sys.argv[2]))
