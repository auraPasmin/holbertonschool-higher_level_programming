#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by:
(based on 1-rectangle.py)
"""


class Rectangle:
    """pass"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """property"""
        return self.__width

    @property
    def height(self):
        """property"""
        return self.__height

    @width.setter
    def width(self, value):
        """getter and setter"""
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """getter and setter"""
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area"""
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """the perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        perimeter = (self.__height * 2) + (self.__width * 2)
        return perimeter
