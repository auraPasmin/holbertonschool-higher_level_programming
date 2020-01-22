#!/usr/bin/python3
"""Write a function that returns the number of lines of a text file:"""


def number_of_lines(filename=""):
    """args:
    line: variable"""
    li = 0
    with open(filename) as f:
        for line in f:
            li += 1
    return li
