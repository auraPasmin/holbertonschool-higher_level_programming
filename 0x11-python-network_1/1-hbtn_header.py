#!/usr/bin/python3
"""value of the X-Request-Id variable found in the header of the response."""
from urllib.request import argv
import sys

if __name__ == "__main__":
    url = urllib.request.Request(argv[1])
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))