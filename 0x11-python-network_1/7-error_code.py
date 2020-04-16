#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
