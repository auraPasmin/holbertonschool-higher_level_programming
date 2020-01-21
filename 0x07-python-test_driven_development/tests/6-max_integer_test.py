#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittest for max_integer """
    def test_list_order(self):
        """ Test a list """
	list = [1, 2, 3, 4, 5]
	self.assertEqual(max_integer(list), 5)

    def test_list_empty(self):
	""" Test a empty list"""
	list = []
	self.assertEqual(max_integer(list), None)

    def test_list_unorder(self):
	""" Test a list unorder"""
	list = [1, 3, 2, 4, 5]
	self.assertEqual(max_integer(list), 5)

    def test_one_item(self):
	""" Test one element"""
	list = [1]
	self.assertEqual(max_integer(list), 1)

    def test_float(self):
	""" Test float """
	list = [3.21, 3.22, 33.3, 43.2]
	self.assertEqual(max_integer(list), 43.2)

    def test_string(self):
        """ Test String"""
	string = "Test"
	self.assertEqual(max_integer(string), "Test")

    def test_list_string(self):
        """ Test String"""
	list = ["Test", "max", "Betty"]
	self.assertEqual(max_integer(list), "max")

    if __name__ == "__main__":
        unittest.main()
