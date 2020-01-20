#!/usr/bin/python3
""" Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):

        """
        Args:
        size: size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
