#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of respons
"""

from urllib import error, request
from sys import argv

if __name__ == "__main__":
    url = request.Request(argv[1])

    try:
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
