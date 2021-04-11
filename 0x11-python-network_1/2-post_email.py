#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""
import urllib.request as req
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    email = argv[2]
    data = parse.urlencode({'email': email}).encode('utf-8')
    url = req.Request(argv[1], data)
    with req.urlopen(url) as res:
        print(res.read().decode('utf-8'))
