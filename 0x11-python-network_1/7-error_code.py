#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    if int(res.status_code) < 400:
        print(rest.text)
    else:
        print("Error code: {}".format(res.status_code))
