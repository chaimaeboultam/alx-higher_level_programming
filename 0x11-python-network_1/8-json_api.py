#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a string and sends a search request to the Star Wars API
    """
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    payload = {'q': q}

    r = requests.post(url, data=payload)
    try:
        json_response = r.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

