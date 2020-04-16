#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        data = {'q': ''}
    else:
        data = {'q': '{}'.format(argv[1])}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        user = r.json()
        if user:
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
