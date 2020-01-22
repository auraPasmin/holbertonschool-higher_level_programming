#!/usr/bin/python3
""" Write a function that returns an object (Python data structure)
represented by a JSON string:"""
import json


def save_to_json_file(my_obj, filename):
    """json"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
