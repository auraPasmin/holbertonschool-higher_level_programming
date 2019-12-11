#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastn = abs(number) % 10 * -1
else:
    lastn = number % 10
if number > 5:
    print("Last digit of {} is {} and is\
    greater than 5".format(number, lastn))
elif number == 0:
    print("Last digit of {} is\
    {} and is 0".format(number, lastn))
else:
    print("Last digit of {} is {} and is less\
    than 6 and not 0".format(number, lastn))
