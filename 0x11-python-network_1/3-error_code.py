#!/usr/bin/python3
"""Write a Python script that takes in a URL"""

import urllib.error
from sys import argv
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
