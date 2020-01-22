#!/usr/bin/python3
"""write a function tha returns the JSON"""
import json


def to_json_string(my_obj):
    """representation of an object (string):"""
    return json.dumps(my_obj)
