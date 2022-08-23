#!/usr/bin/python3
""" Displays the value of the variable X-Request-Id. """


import requests
from sys import argv


response = requests.get(argv[1])
print(response.headers['X-Request-Id'])
