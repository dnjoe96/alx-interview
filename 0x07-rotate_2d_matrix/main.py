#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3, 1],
              [4, 5, 6, 4],
              [7, 8, 9, 0],
              [8, 9, 0, 1]]

    rotate_2d_matrix(matrix)
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])
