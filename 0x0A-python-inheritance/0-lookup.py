#!/usr/bin/python3
""" function that returns the list of available attributes and methods """


def lookup(obj):
    """Returns a list object"""
    return(dir(obj))
