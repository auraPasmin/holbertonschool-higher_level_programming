#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)
7 and returns the number of characters written:"""


def append_write(filename="", text=""):
    """that writes a string to a text file (UTF8)
    args:
    filename"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
