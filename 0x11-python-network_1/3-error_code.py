#!/usr/bin/python3
"""
    Accepts URL n sends request
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            if response:
                html = response.read()
                print(html.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
