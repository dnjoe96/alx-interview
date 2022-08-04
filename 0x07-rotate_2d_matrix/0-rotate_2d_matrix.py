#!/usr/bin/python3
""" Module for rotate matrix function """


def rotate_2d_matrix(matrix):
    """ The function takes a 2D matrix
        and rotates it 90 degree.

        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    """
    n = len(matrix)
    for x in range(0, int(n / 2)):

        for y in range(x, n - x - 1):
            # print((x,y))
            tmp = matrix[x][y]

            # print((x,y), (n - 1 - y,x))
            matrix[x][y] = matrix[n - 1 - y][x]

            # print((n - 1 - y,x), (n - 1 - x,n - 1 - y))
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]

            # print((n - 1 - x,n - 1 - y), (y,n - 1 - x))
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]

            # print((y,n - 1 - x))
            matrix[y][n - 1 - x] = tmp
