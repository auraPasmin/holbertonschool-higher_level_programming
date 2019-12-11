#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    l = number % 10
else:
    l = abs(number) % 10 * -1
if number > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, l))
elif number == 0:
    print("Last digit of {} is {} and is 0".format(number, l))
else:
    print("Last digit of {} is {}".format(number, l), end="")
    print("and is less than 6 and not 0")
