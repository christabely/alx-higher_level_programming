#!/usr/bin/python3
"""
Takes letter, sends to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    q = sys.argv[1] if len(sys.argv) >= 2 else ""

    response = requests.post(url, data={'q': q})
    try:
        kd = response.json()
        if kd:
            print("[{}] {}".format(kd.get('id'), kd.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
