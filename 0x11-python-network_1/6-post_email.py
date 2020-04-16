#!/usr/bin/python3
""" """

from sys import argv
import requests

if __name__ == "__main__":
    email = {'email': '{}'.format(argv[2])}
    res = requests.post(argv[1], data=email)
    print(res.text)
