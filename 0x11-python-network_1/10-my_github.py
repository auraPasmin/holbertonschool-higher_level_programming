#!/usr/bin/python3
""" """

import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(res.json().get('id'))
