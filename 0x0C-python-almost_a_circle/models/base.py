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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json metohd"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file = cls.__name__ + ".json"
        empty = []
        if list_objs:
            for i in list_objs:
                empty.append(cls.to_dictionary(i))
        with open(file, "w") as w:
            w.write(cls.to_json_string(empty))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            from models.rectangle import Rectangle
            obj = Rectangle(1, 1)
        elif cls.__name__ is "Square":
            from models.square import Square
            obj = Square(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = cls.__name__ + ".json"
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
