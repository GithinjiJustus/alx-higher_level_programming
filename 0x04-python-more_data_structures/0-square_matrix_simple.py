#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    
    Args:
        matrix: A 2 dimensional array
    
    Returns:
        A new matrix of the same size as input matrix with each value squared
        The initial matrix should not be modified
    """
    return [[num * num for num in row] for row in matrix]

# For testing the function
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
