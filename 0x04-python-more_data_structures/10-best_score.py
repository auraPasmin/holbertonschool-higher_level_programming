#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        core = max(a_dictionary.values())
        return[i for i, num in a_dictionary.items() if num == core][0]
