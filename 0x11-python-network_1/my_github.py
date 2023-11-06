#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    auth = HTTPBasicAuth(username, token)
    response = requests.get(url, auth=auth)
    id = response.json().get('id')
    print(id)
