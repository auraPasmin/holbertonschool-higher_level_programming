#!/usr/bin/python3
"""
add-integer Module
adds two integers
"""


def add_integer(a, b=98):
    """This function returns the result of an addition between two
    integers or error if the parameters are not integers or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return int(a)+int(b)
