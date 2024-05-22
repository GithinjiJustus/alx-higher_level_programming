#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable in the response header using the requests package."""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
