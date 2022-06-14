#!/usr/bin/python3
""" The module contains a function that return a pascal triange """


def pascal_triangle(n):
    """ A function that return a list of pascal triange
    rows given an integer
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        lis = [1]
        if i == 1:
            lis.append(1)
        else:
            for x in range(i - 1):
                lis.append(triangle[-1][x] + triangle[-1][x+1])

            lis.append(1)

        triangle.append(lis)

    return triangle
