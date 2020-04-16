#!/usr/bin/python3
"""value of the X-Request-Id variable found in the header of the response."""
import urllib.request
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        p = response.getheader("X-Request-Id")
    print(p)
