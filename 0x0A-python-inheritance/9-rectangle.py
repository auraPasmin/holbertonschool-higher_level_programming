#!/usr/bin/python3
""" Class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):

        """Args:
        width: width of rectangle
        height: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ Return description of rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
