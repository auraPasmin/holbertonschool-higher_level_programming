#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ky = [k for k, val in a_dictionary.items() if val == value]
    if ky:
        for element in ky:
            del a_dictionary[element]
    return a_dictionary
