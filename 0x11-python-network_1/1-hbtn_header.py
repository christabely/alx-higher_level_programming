#!/usr/bin/python3
"""
    displays value of X-Request-Id variable
"""
import urllib.request
import sys


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            if response:
                value = response.headers.get('X-Request-Id')
                print(value)
    except BaseException:
        pass
