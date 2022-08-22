#!/usr/bin/python3
"""
script that takes in a URL, sends a
request to the URL and displays a value
"""
from urllib.request import urlopen
import sys


if __name__ == "__main__":

    with urlopen(sys.argv[1]) as response:
        info = response.info()
        print(info.get("X-Request-Id"))
