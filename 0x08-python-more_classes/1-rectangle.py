#!/usr/bin/python3
"""Write a class Rectangle that defines
a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """property def width(self): to retrieve it
    property def height(self): to retrieve it
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter and setter"""
        return self.__width

    @property
    def height(self):
        """value"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter and getter"""
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter and getter"""
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
