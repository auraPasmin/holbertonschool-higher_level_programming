#!/usr/bin/python3
"""
print square Module
print a square with the character #
"""


def print_square(size):
    """ print a square with the character #
    using the parameter size  number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
