#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry():
    """class"""
    def area(self):
        """area
        Args:
        name: string.
        value: value.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if(value < 1):
            raise ValueError("{} must be greater than 0".format(name))
