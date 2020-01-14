#!/usr/bin/python3
"""
 that divides all each element of a matrix by a divisor
"""


def matrix_divided(matrix, div):
    """
    This returns a new matrix
    """
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists)'
			' of integers/floats')
    if not all(isinstance(rows, list) for rows in matrix):
        raise TypeError('matrix must be a matrix (list of lists)'
		        ' of integers/floats')
    for rows in matrix:
        if not all(isinstance(cols, (float, int)) for cols in rows):
            raise TypeError('matrix must be a matrix (list of lists)'
		            ' of integers/floats')
    if not all(len(rows) == len(matrix[0]) for rows in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    result = [[round(cols/div, 2) for cols in rows] for rows in matrix]
    return result
