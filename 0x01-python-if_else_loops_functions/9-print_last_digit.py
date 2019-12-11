#!/usr/bin/python3
def print_last_digit(number):
    lastn = abs(number) % 10
    print("{}".format(lastn), end="")
    return(lastn)
