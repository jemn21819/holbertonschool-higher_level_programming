#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
"""
import requests as req
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = (argv[1], argv[2])
    res_json = req.get(url, auth=user).json()
    print(res_json.get('id'))
