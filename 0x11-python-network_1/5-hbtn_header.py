#!/usr/bin/python3
""" Write a Python script that takes in a URL """

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    p = requests.get(p)
    print(p.headers.get('X-Request-Id'))
