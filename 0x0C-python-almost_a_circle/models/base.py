#!/usr/bin/python3
""" class base """
import json
from os import path


class Base:
    """ class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class initializer"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """representation of list_dictionaries:"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
