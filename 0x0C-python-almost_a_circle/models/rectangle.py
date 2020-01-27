#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """initializer builder"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter and Setter"""
        return self.__width

    @property
    def height(self):
        """Getter and Setter"""
        return self.__height

    @property
    def x(self):
        """Getter and Setter"""
        return self.__x

    @property
    def y(self):
        """Getter and Setter"""
        return self.__y
