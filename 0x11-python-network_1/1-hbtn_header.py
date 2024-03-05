#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the
response
"""
import urlib.request
import sys

if  __name__ == "__main__":
    url = sys.argv[1]

    with urlib.request.urlopen(url) as respnse:
        print(response.headers.get('X-Request-Id'))
