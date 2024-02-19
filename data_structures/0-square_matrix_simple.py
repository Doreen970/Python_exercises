#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    second_mat = []
    for row in matrix:
        squared_row = [int(x) ** 2 for x in row]
        second_mat.append(squared_row)
    return second_mat
