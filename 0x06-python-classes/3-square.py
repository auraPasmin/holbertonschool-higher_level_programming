#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        """Return area"""
        return self.__size * self.__size
