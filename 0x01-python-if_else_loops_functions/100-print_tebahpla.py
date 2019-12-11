#!/usr/bin/python3
u = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - u)), end="")
    u = 32 if u == 0 else 0
