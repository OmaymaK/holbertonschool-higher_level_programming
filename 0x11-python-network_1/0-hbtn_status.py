#!/usr/bin/python3
"""
a Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request as u


if __name__ == '__main__':
    with u.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
