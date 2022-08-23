#!/usr/bin/python3
"""Displays the value of the variable X-Request-Id."""
import requests
import sys

response = requests.get(sys.argv[1])
print(response.headers['X-Request-Id'])
