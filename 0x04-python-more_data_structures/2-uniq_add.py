#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = list(dict.fromkeys(my_list))
    return sum(uniq)
