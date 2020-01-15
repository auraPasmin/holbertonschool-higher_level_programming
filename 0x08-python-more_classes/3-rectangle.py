#!/usr/bin/python3
""" Write a class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)"""


class Rectangle():
    """pass"""
    def __init__(self, width=0, height=0):
        """the class Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """area of the Rectangle"""
        return self.height * self.width

    def perimeter(self):
        """ perimeter of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.height + self.height + self.width + self.width

    @property
    def width(self):
        """getter and setter"""
        return self.__width__

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width__ = value

    @property
    def height(self):
        """The height"""
        return self.__height__

    @height.setter
    def height(self, value):
        """Setter an getter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height__ = value

    def __str__(self):
        """Class as a String"""
        strg = ''
        for i in range(self.height):
            strg += '#' * self.width + '\n'
        strg = strg.rstrip()
        return strg
