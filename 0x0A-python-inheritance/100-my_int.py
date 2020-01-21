#!/usr/bin/python3
""" Change the operator."""


class MyInt(int):
    """ Class MyInt """

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
