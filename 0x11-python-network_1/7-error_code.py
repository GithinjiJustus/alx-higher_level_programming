#!/usr/bin/python3
"""Displays the body of the response and handles HTTPError exceptions using the requests package."""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
