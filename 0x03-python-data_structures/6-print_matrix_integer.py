#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    #  Iterate through each row in the matrix
    for row in matrix:
        #  Iterate through each column in the row
        for col in row:
            #  Print the integer with formatting
            print("{:d}".format(col), end=" " if col != row[-1] else "")
            #  Print a space after the integer if it's not last element in row
            #  Move to the next line after printing all columns in the row
            print ()
