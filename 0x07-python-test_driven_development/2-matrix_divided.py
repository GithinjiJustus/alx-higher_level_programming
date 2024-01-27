#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, divisor):
    """
    Divide each element of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        divisor (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numeric elements.
        TypeError: If the matrix rows have different sizes.
        TypeError: If the divisor is not an integer or float.
        ZeroDivisionError: If the divisor is 0.

    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, (int, float)) for row in matrix for ele in row)):
        raise TypeError("Input matrix must be a non-empty matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(divisor, (int, float)):
        raise TypeError("Divisor must be a numeric value")

    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    result_matrix = [[round(elem / divisor, 2) for elem in row] for row in matrix]
    return result_matrix
