#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
"""
import requests as req
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    res = req.get(url)
    commit = res.json()
    for com in commit[:10]:
        sha = com.get('sha')
        author_name = com.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
