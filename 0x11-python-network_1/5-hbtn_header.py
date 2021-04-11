#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
"""
import requests as req
from sys import argv

if __name__ == "__main__":
    url = req.get(argv[1])
    print(url.headers.get('X-Request-Id'))
