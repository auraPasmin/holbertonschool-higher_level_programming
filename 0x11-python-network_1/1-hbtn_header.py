#!/usr/bin/python3
"""value of the X-Request-Id variable found in the header of the response."""
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    url = urllib.request.Request(argv[1])
    with urlopen(url) as response:
        header = response.getheader("X-Request-Id")
    print(header)
