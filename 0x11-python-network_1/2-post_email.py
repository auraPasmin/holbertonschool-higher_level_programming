#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        email = response.read()
    print(email.decode('utf-8'))
