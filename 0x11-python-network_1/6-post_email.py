#!/usr/bin/python3
"""  lists value of variable in header of response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.post(url, data={'email': sys.argv[2]})
    print(response.text)
