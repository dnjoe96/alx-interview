#!/usr/bin/env python3
""" Module for minOperations function """


def minOperations(n):
    """ The function finds the minimum operations to create n
    characters in a note"""
    res = 0

    for i in range(2, n + 1):
        # print('res = ', res, 'i = ', i)
        # print('n = ', int(n))

        while(n % i == 0):
            # check if problem can be broken into smaller problem
            # if yes then add no of smaller problems to result.
            res += i
            # create smaller problem
            n = n / i

            if n == 1:
                break
            # print(int(n))
    return res
