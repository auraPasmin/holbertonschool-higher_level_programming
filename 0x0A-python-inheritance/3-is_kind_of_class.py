#!/usr/bin/python3
""" returns True if the object is an instance of, or
is an instance of a class otherwise False.
"""


def is_kind_of_class(obj, a_class):
        """
        Args:
        obj: a object.
        a_class: a Class.
        Return: True or False.
        """
        return True if isinstance(obj, a_class) else false
