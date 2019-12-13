#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv)
    if count == 1:
        print("0 arguments.")
    if count == 2:
        print("{} argument:".format(count - 1))
    if count > 2:
        print("{} arguments:".format(count - 1))
    for i in range(1, count):
        print("{}: {}".format(i, sys.argv[i]))
